from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView

from cart.models import CartProduct, Cart
from core.forms import OrderForm
from core.models import Cake
from orders.models import Order


class MyCart(TemplateView):
    template_name = 'MyCart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        return context


class AddToCartView(View):
    def get(self, request, **kwargs):
        cake_id = self.kwargs['cake_id']
        cake_obj = Cake.objects.get(id=cake_id)

        # check if cart exists
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            this_cake_in_cart = cart_obj.cartproduct_set.filter(cake=cake_obj)

            # items already in cart
            if this_cake_in_cart.exists():
                cartproduct = this_cake_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += cake_obj.price
                cartproduct.save()
                cart_obj.total += cake_obj.price
                cart_obj.save()

                # if new item added in cart
            else:
                cartproduct = CartProduct.objects.create(
                    cart=cart_obj, cake=cake_obj, rate=cake_obj.price, quantity=1,
                    subtotal=cake_obj.price)
                cart_obj.total += cake_obj.price
                cart_obj.save()

        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            cartproduct = CartProduct.objects.create(cart=cart_obj, cake=cake_obj, rate=cake_obj.price, quantity=1,
                                                     subtotal=cake_obj.price)
            cart_obj.total += cake_obj.price
            cart_obj.save()
            messages.info(request, 'Item added into cart successfully')
            return render(request, 'MyCart.html', {'cart_obj': cart_obj})
        return redirect('MyCart')


class ManageCart(View):
    def get(self, request, cp_id):
        action = request.GET.get("action")
        cp_obj = CartProduct.objects.get(id=cp_id)
        cart_obj = cp_obj.cart
        if action == 'inc':
            cp_obj.quantity += 1
            cp_obj.subtotal += cp_obj.rate
            cp_obj.save()
            cart_obj.total += cp_obj.rate
            cart_obj.save()
        elif action == 'dcr':
            cp_obj.quantity -= 1
            cp_obj.subtotal -= cp_obj.rate
            cp_obj.save()
            cart_obj.total -= cp_obj.rate
            cart_obj.save()
            if cp_obj.quantity == 0:
                cp_obj.delete()

        elif action == 'rmv':
            cart_obj.total -= cp_obj.subtotal
            cart_obj.save()
            cp_obj.delete()
        else:
            pass
        return redirect('MyCart')


class CheckoutView(CreateView, LoginRequiredMixin):
    template_name = 'checkout.html'
    form_class = OrderForm
    success_url = reverse_lazy('MyOrders')
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
        else:
            cart = None
        context['cart'] = cart
        return context

    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id', None)
        if cart_id:
            cart = Cart.objects.get(id=cart_id)
            form.instance.cart = cart
            form.instance.user = self.request.user
            number = form.cleaned_data.get('mobile')
            mobile = number.replace("0", "254", 1)
            form.instance.mobile = mobile
            form.instance.total = cart.total
            form.instance.order_status = 'pending'
            del self.request.session['cart_id']
        else:
            cart = None
        return super().form_valid(form)

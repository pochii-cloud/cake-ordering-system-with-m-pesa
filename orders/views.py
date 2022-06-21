import requests
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, DeleteView

from orders.models import Order


class MyOrders(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        orders = Order.objects.all().filter(user=request.user)
        return render(request, 'my_orders.html', {'orders': orders})

    # def post(self, request):
    #     order = Order.objects.get(id=request.POST['order_id'])
    #     res = requests.post('http://localhost:8000/mpesa/online/lipa/',
    #                         data={'PhoneNumber': order.mobile, 'Amount': order.total})
    #     return redirect('BaseView')


class CancelOrder(DeleteView):
    model = Order
    success_url = '/'
    template_name = 'delete.html'

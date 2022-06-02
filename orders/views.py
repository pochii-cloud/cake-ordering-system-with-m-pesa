from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from orders.models import Order


class MyOrders(LoginRequiredMixin, View):
    login_url = '/accounts/LoginPageView/'

    def get(self, request):
        orders = Order.objects.all().filter(user=request.user)
        return render(request, 'my_orders.html', {'orders': orders})

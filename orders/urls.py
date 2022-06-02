from django.urls import path

from orders.views import MyOrders

urlpatterns = [
    path('', MyOrders.as_view(), name='MyOrders')
]

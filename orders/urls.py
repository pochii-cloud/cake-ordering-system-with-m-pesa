from django.urls import path

from orders.views import MyOrders, CancelOrder

urlpatterns = [
    path('', MyOrders.as_view(), name='MyOrders'),
    path('CancelOrder/<int:pk>/', CancelOrder.as_view(), name='CancelOrder')
]

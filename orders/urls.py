from django.urls import path

from orders.views import Myorders

urlpatterns = [
    path('', Myorders.as_view(), name='Myorders')
]

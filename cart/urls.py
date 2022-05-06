from django.urls import path

from cart.views import MyCart, ManageCart, AddToCartView

urlpatterns = [
    path('MyCart/', MyCart.as_view(), name='MyCart'),
    path('ManageCart/<int:cp_id>/', ManageCart.as_view(), name='ManageCart'),
    path('AddToCartView/<int:cake_id>/', AddToCartView.as_view(), name='AddToCartView'),
]

from django.contrib import admin

# Register your models here.
from cart.models import CartProduct, Cart

admin.site.register(Cart)
admin.site.register(CartProduct)

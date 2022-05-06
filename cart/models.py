from django.db import models

# Create your models here.
from core.models import Cake


class Cart(models.Model):
    total = models.PositiveIntegerField(default=0)

    def __str__(self):
        return "Cart" + str(self.id)


class CartProduct(models.Model):
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    rate = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    subtotal = models.PositiveIntegerField()

    def __str__(self):
        return  "CartProducts" + str(self.id)

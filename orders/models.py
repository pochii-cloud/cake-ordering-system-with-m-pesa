from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from cart.models import Cart

Order_Status = [
    ('delivered', 'delivered'),
    ('pending', 'pending')
]


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE)
    ordered_by = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    total = models.PositiveIntegerField()
    order_status = models.CharField(max_length=100, choices=Order_Status)

    def __str__(self):
        return "order" + str(self.id)


    class Meta:
        verbose_name_plural = 'Orders'

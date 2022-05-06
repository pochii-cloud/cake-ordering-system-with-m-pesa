from django.db import models


# Create your models here.

class Cake(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=8, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cakes'


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contacts'

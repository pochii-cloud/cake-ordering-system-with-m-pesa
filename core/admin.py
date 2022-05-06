from django.contrib import admin

# Register your models here.
from core.models import Contact, Cake

admin.site.register(Cake)
admin.site.register(Contact)

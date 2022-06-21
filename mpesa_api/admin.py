from django.contrib import admin

# Register your models here.
from mpesa_api.models import MpesaCalls, MpesaCallBacks, MpesaPayment

admin.site.register(MpesaCalls)
admin.site.register(MpesaCallBacks)
admin.site.register(MpesaPayment)

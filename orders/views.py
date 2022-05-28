from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Myorders(TemplateView):
    template_name = 'vendor_login.html'

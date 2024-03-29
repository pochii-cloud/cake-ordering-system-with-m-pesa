from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from orders.models import Order


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'pass', type: 'password'}),
            'password2': forms.PasswordInput(attrs={'class': 'pass', type: 'password'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['ordered_by', 'shipping_address', 'mobile']

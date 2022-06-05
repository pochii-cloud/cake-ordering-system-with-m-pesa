from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from core.forms import RegisterForm


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'vendor-new.html'
    success_url = reverse_lazy('LoginPageView')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginPageView(LoginView):
    template_name = 'vendor_login.html'


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')


class AdminLoginView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request):
        return redirect('ManageCakes')

    def post(self, request):
        return redirect('ManageCakes')

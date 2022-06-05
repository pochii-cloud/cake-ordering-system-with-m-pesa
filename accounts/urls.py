from django.urls import path

from accounts.views import RegisterView, LoginPageView, LogoutView, AdminLoginView
from core.views import *

urlpatterns = [
    path('RegisterView/', RegisterView.as_view(), name='RegisterView'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('AdminLoginView/', AdminLoginView.as_view(), name='AdminLoginView'),
    path('LogoutView/', LogoutView.as_view(), name='LogoutView'),
]

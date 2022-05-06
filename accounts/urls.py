from django.urls import path

from accounts.views import RegisterView, LoginPageView, LogoutView
from core.views import *

urlpatterns = [
    path('RegisterView/', RegisterView.as_view(), name='RegisterView'),
    path('LoginPageView/', LoginPageView.as_view(), name='LoginPageView'),
    path('LogoutView/', LogoutView.as_view(), name='LogoutView'),
]

from django.urls import path

from core.views import *

urlpatterns = [
    path('', BaseView.as_view(), name='BaseView'),
    path('ServicesView/', ServicesView.as_view(), name='ServicesView'),
    path('AboutUs/', AboutUs.as_view(), name='AboutUs'),
    path('ContactUs/', ContactUs.as_view(), name='ContactUs'),
    path('Footer/', Footer.as_view(), name='Footer'),
    path('DeleteCake/<int:pk>/', DeleteCake.as_view(), name='DeleteCake'),
    path('ManageCakes/', ManageCakes.as_view(), name='ManageCakes'),
    path('AddCake/', AddCake.as_view(), name='AddCake'),
    path('UpdateCakeDetails/<int:pk>/', UpdateCakeDetails.as_view(), name='UpdateCakeDetails'),

]

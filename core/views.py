from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, DeleteView, UpdateView

from core.models import Contact, Cake


class BaseView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cake'] = Cake.objects.all()[:5]
        return context


class ServicesView(TemplateView):
    template_name = 'services.html'


class AboutUs(TemplateView):
    template_name = 'aboutus.html'


class ContactUs(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact()
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.message = message
        contact.save()
        return HttpResponse('request sent')


class Footer(TemplateView):
    template_name = 'footer.html'


class AdminLoginView(LoginView):
    template_name = 'admin.html'


class ManageCakes(TemplateView):
    template_name = 'manage_cakes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cake'] = Cake.objects.all()
        return context


class AddCake(View):
    def get(self, request):
        return render(request, 'manage_cakes.html')

    def post(self, request):
        cake_name = request.POST.get('cake_name')
        cake_price = request.POST.get('cake_price')
        cake_description = request.POST.get('cake_description')
        cake_image = request.FILES['cake_image']
        cake = Cake()
        cake.name = cake_name
        cake.price = cake_price
        cake.description = cake_description
        cake.image = cake_image
        cake.save()
        return HttpResponse('cake added successfully')


class DeleteCake(DeleteView):
    template_name = 'deletecake.html'
    model = Cake
    success_url = '/'


class UpdateCakeDetails(UpdateView):
    template_name = 'update_cake_details.html'
    model = Cake
    fields = ['name', 'image', 'description', 'price']
    success_url = '/'

from django.shortcuts import render
from django.views.generic.edit import UpdateView
from serviceProviderApp.models import Kitchen2Register

# Create your views here.
class KitchenUpdate(UpdateView):
    model=Kitchen2Register
    fields=['workingDays']
    template_name = 'serviceProviderApp/kitchenUpdate.html'

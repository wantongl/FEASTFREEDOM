from django.shortcuts import render
from django.views.generic.edit import UpdateView
from serviceProviderApp.models import Kitchen2Register

# Create your views here.
class KitchenUpdate(UpdateView):
    model=Kitchen2Register
    fields=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','startTime','endTime']
    template_name = 'serviceProviderApp/kitchenUpdate.html'
    success_url = '..'

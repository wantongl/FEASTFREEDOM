from django.shortcuts import render
from django.views.generic.edit import UpdateView
from serviceProviderApp.models import Kitchen2Register

# Create your views here.
class KitchenUpdate(UpdateView):
    model=Kitchen2Register
    fields=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','mondayStartTime','mondayEndTime','tuesdayStartTime','tuesdayEndTime','wednesdayStartTime','wednesdayEndTime','thursdayStartTime','thursdayEndTime','fridayStartTime','fridayEndTime','saturdayStartTime','saturdayEndTime','sundayStartTime','sundayEndTime']
    template_name = 'serviceProviderApp/kitchenUpdate.html'
    success_url = '..'

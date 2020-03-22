from django.shortcuts import render
from django.views.generic.edit import UpdateView
from serviceProviderApp.models import Kitchen2Register
from django.http import HttpResponseRedirect

# Create your views here.
class KitchenUpdate(UpdateView):
    model=Kitchen2Register
    fields=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','mondayStartTime','mondayEndTime','tuesdayStartTime','tuesdayEndTime','wednesdayStartTime','wednesdayEndTime','thursdayStartTime','thursdayEndTime','fridayStartTime','fridayEndTime','saturdayStartTime','saturdayEndTime','sundayStartTime','sundayEndTime']
    template_name = 'serviceProviderApp/kitchenUpdate.html'
    success_url = '..'

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(KitchenUpdate, self).post(request, *args, **kwargs)

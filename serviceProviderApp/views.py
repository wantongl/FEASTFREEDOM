from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from serviceProviderApp.models import Kitchen2Register
from django.http import HttpResponseRedirect
from . import forms
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def ProviderRegisterView(request):
    if request.method == "POST":
        form = forms.ProviderRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # form.instance.username
            username = form.cleaned_data.get('username')
            messages.success(request, f'Registered Success for {username}')

            raw_password = form.clean_password2()
            user = authenticate(username=username, password=raw_password)
            login(request, user)

            return redirect('serviceProviderApp:kitchenUpdate')
    else:
        form = forms.ProviderRegisterForm()
    return render(request, 'serviceProviderApp/providerSignUp.html', {'form': form})

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

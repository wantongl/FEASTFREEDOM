from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Kitchen2Register

class ProviderRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #QPGdP7RSSrazv6i
    class Meta:
        #model=Kitchen2Register
        #fields=('name','email')
        model = User
        fields = ("username", "email", "password1", "password2")
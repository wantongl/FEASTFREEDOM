from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from .forms import RegularUserCreation


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username','password','email','last_login',
    'is_superuser','is_staff','is_active','question1','answer1','question2','answer2']


admin.site.register(User, UserAdmin)
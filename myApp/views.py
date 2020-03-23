from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'myApp/base.html', {'Home_Text': "Welcome to FEASTFREEDOM!  Be a Feast Beast!"})

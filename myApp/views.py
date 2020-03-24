from django.http import HttpResponse
from django.shortcuts import render
from cart.forms import CartAddProductForm
from cart.cart import Cart
from serviceProviderApp.models import Kitchen2Register

# Create your views here.

def index(request):
	#cart_product_form = CartAddProductForm()
	cart = Cart(request)
	if request.POST:
		k = Kitchen2Register.objects.all()  # filter(available=True)
		return render(request, 'userModule/kitchen_list.html', {'kitchens': k, 'cart': cart})
	else:
		# return render(request,'shop/product/detail.html',{'product': kitchen,'cart_product_form': cart_product_form})
		#return render(request, 'userModule/kitchen_detail.html',{'kitchen': kitchen, 'cart_product_form': cart_product_form})
		return render(request,'myApp/home.html', {'cart': cart})


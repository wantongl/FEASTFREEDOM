from django.http import HttpResponse
from django.shortcuts import render
from cart.forms import CartAddProductForm
from cart.cart import Cart

# Create your views here.

def index(request):
	#cart_product_form = CartAddProductForm()
	cart = Cart(request)
	# return render(request,'shop/product/detail.html',{'product': kitchen,'cart_product_form': cart_product_form})
	#return render(request, 'userModule/kitchen_detail.html',{'kitchen': kitchen, 'cart_product_form': cart_product_form})
	return render(request,'myApp/base.html', {'Home_Text': "Welcome to FEASTFREEDOM!  Be a Feast Beast!", 'cart': cart})

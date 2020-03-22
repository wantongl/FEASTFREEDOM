from django.shortcuts import render,get_object_or_404
from userModule.models import Kitchen

# Create your views here.
def kitchen_list(request):
    #category = None
    #categories = Category.objects.all()
    k = Kitchen.objects.all() #filter(available=True)
    #if category_slug:
    #    category = get_object_or_404(Category, slug=category_slug)
    #    products = products.filter(category=category)
    #return render(request, 'userModule/kitchen_list.html', {'category': category,'categories': categories,'products': products})
    return render(request, 'userModule/kitchen_list.html',{'kitchens':k})

#def kitchen_detail(request, id, slug):
def kitchen_detail(request, id):
    #product = get_object_or_404(Product, id=id, slug=slug, available=True)
    kitchen = get_object_or_404(Kitchen, id=id)
    #cart_product_form = CartAddProductForm()
    #return render(request,'shop/product/detail.html',{'product': kitchen,'cart_product_form': cart_product_form})
    return render(request, 'userModule/kitchen_detail.html', {'product': kitchen})
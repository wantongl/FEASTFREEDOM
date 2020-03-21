from django.shortcuts import render
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
    return render(request, 'userModule/kitchen_list.html','kitchens':k)
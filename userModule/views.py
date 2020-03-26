from django.shortcuts import render,get_object_or_404, redirect
#from userModule.models import Kitchen
from django.urls import reverse
from serviceProviderApp.models import Kitchen2Register,menuItem
from cart.forms import CartAddProductForm
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from userModule.forms import RegularUserCreation
from cart.cart import Cart
from django.http import HttpResponseRedirect,HttpResponse

# Create your views here.
def kitchen_list(request):
    #category = None
    #categories = Category.objects.all()
    k = Kitchen2Register.objects.all() #filter(available=True)
    cart = Cart(request)
    #if category_slug:
    #    category = get_object_or_404(Category, slug=category_slug)
    #    products = products.filter(category=category)
    #return render(request, 'userModule/kitchen_list.html', {'category': category,'categories': categories,'products': products})
    return render(request, 'userModule/kitchen_list.html',{'kitchens':k,'cart':cart})

def kitchen_detail(request, id):
    kitchen = get_object_or_404(Kitchen2Register, id=id)
    #for t in kitchen.menu.all():
    #    print(t.id)
    cart_product_form = CartAddProductForm()
    cart = Cart(request)
    if "cancel" in request.POST:
        url='..'
        return HttpResponseRedirect(url)
    else:
        #return render(request,'shop/product/detail.html',{'product': kitchen,'cart_product_form': cart_product_form})
        return render(request, 'userModule/kitchen_detail.html', {'kitchen': kitchen, 'cart_product_form': cart_product_form,'cart':cart})

#def createMenuItem(request,id):
#    k=Kitchen2Register.objects.get(id)
#    m=k.menu_set.create()

class createMenuItem(CreateView):
    model=menuItem
    fields=['name','veg','price']
    template_name = 'userModule/create_menuItem.html'

    def get_success_url(self):
        k=Kitchen2Register.objects.latest('id')
        return reverse('serviceProviderApp:kitchenUpdate', args=(k.id,))

    success_url = get_success_url

class updateMenuItem(UpdateView):
    model=menuItem
    fields=['name','veg','price']
    template_name = 'userModule/edit_menuItem.html'

    def get_success_url(self):
        k=Kitchen2Register.objects.latest('id')
        return reverse('userModule:kitchen_detail', args=(k.id,))

    success_url = get_success_url

class deleteMenuItem(DeleteView):
    model=menuItem
    fields=['name','veg','price']
    template_name = 'userModule/delete_menuItem.html'

    def get_success_url(self):
        k=Kitchen2Register.objects.latest('id')
        return reverse('userModule:kitchen_detail', args=(k.id,))

    success_url = get_success_url

class createKitchen(CreateView):
#class createKitchen(UpdateView):
    model=Kitchen2Register
    #fields=['name','email','image','description','menu','monday','tuesday','wednesday','thursday','friday','saturday','sunday','mondayStartTime','mondayEndTime','tuesdayStartTime','tuesdayEndTime','wednesdayStartTime','wednesdayEndTime','thursdayStartTime','thursdayEndTime','fridayStartTime','fridayEndTime','saturdayStartTime','saturdayEndTime','sundayStartTime','sundayEndTime']
    fields=['username','name','email']
    template_name = 'serviceProviderApp/kitchenCreate.html'

    def get_success_url(self):
        #print(self.object.id)
        return reverse('serviceProviderApp:kitchenUpdate', args=(self.object.id,))

    def post(self, request, *args, **kwargs):
        #   self.object=self.get_object(id=args)
        if "cancel" in request.POST:
            url = '..' #self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(createKitchen, self).post(request, *args, **kwargs)
            #return HttpResponse("Success!")
            #url = self.get_success_url()#reverse('serviceProviderApp:kitchenUpdate', args=(self.object.id,))
            #return HttpResponseRedirect(url)

    success_url = get_success_url

class updateRegisteredKitchen(UpdateView):
    model=Kitchen2Register
    fields=['name','email','image','description','menu','monday','tuesday','wednesday','thursday','friday','saturday','sunday','mondayStartTime','mondayEndTime','tuesdayStartTime','tuesdayEndTime','wednesdayStartTime','wednesdayEndTime','thursdayStartTime','thursdayEndTime','fridayStartTime','fridayEndTime','saturdayStartTime','saturdayEndTime','sundayStartTime','sundayEndTime']
    template_name = 'serviceProviderApp/kitchenEdit.html'

    def get_success_url(self):
        k=Kitchen2Register.objects.latest('id')
        return reverse('userModule:kitchen_detail', args=(k.id,))

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = '..' #self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(updateRegisteredKitchen, self).post(request, *args, **kwargs)

    success_url = get_success_url

@login_required
def logout(request):
    logout(request)
    return redirect('myApp:index')

def signup(request):
    if request.method == "POST":
        form = RegularUserCreation(request.POST)
        if form.is_valid():
            form.save()
            # form.instance.username
            username = form.cleaned_data.get('username')
            raw_password = form.clean_password2()
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            #return redirect('myApp:index')
            return redirect('userModule:kitchen_list')
    else:
        form = RegularUserCreation()
    return render(request,'userModule/user_signup.html', {'form':form})
from django.conf.urls import include
from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views
#from productApp.views import addProduct,buyProducts,deleteProduct

urlpatterns = [
	re_path(r'^$', views.index, name='index'),
	#url(r'^viewProducts/',views.viewProducts,name='viewProducts'),
	#url(r'^login/', auth_views.LoginView.as_view(template_name='productApp/login.html', success_url='viewProducts/'),name='login'),
	#url(r'^logout/', auth_views.LogoutView.as_view(template_name='productApp/logged_out.html'),name='logout'),
	#url(r'^buyProduct/(?P<pk>\d+)/',views.buyProducts,name='buyProduct'),
	#url(r'^buyProduct/(?P<pk>\d+)/',buyProducts.as_view(),name='buyProduct'),
    #url(r'^removeProduct/(?P<pk>\d+)/$',deleteProduct.as_view(),name='deleteProduct'),
	#url(r'^addProduct/$',addProduct.as_view(),name='addProduct')
]

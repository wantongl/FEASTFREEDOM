from django.urls import path, re_path
from django.conf.urls import include,url
from . import views
from serviceProviderApp.views import KitchenUpdate, ProviderRegisterView
from userModule.views import createMenuItem

urlpatterns = [
    re_path(r'^provider/$',views.ProviderRegisterView, name='providersignup'),
    re_path(r'^provider/(?P<pk>\d+)/$',KitchenUpdate.as_view(),name='kitchenUpdate'),
    url(r'^provider/(?P<id>\d+)/createMenuItem$', createMenuItem.as_view(), name='createMenuItem'),
    #url(r'^$', views.product_list, name='product_list'),
    #url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    #url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]

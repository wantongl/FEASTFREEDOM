from django.conf.urls import url
from . import views
from userModule.views import createMenuItem

urlpatterns = [
    url(r'^$', views.kitchen_list, name='kitchen_list'),
    url(r'^(?P<id>\d+)/$', views.kitchen_detail, name='kitchen_detail'),
    url(r'^(?P<id>\d+)/createMenuItem$', createMenuItem.as_view(), name='createMenuItem'),
    #url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    #url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
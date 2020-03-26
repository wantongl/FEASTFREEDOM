from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from django.urls import reverse
from userModule.views import updateMenuItem

urlpatterns = [
    re_path(r'^$', views.kitchen_list, name='kitchen_list'),
    re_path(r'^(?P<id>\d+)/$', views.kitchen_detail, name='kitchen_detail'),
    re_path(r'^(?P<pk>\d+)/editMenuItem$', updateMenuItem.as_view(), name='editMenuItem'),
    path('signup/',views.signup,name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='userModule/user_login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
    #url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    #url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
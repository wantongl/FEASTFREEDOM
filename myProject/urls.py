"""myProject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include(('myApp.urls','myApp'), namespace='myApp')),
    re_path(r'^provider/', include(('serviceProviderApp.urls','serviceProviderApp'), namespace='serviceProviderApp')),
    re_path(r'^user/', include(('userModule.urls','userModule'), namespace='userModule')),
    re_path(r'^cart/', include(('cart.urls','cart'), namespace='cart')),
    re_path(r'^orders/', include(('orders.urls','orders'), namespace='orders')),
    url(r'^payment/', include(('payment.urls','payment'), namespace='payment')),
    url(r'^paypal/', include('paypal.standard.ipn.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

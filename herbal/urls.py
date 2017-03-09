"""herbal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from login.views import *
from adminpanel.views import home,blog,faqs,prod,sub_query,dealer_cont,customer_cont,seller_cont,sub_query,welcome
from orders.views import addtocart,cartlist,updatecart,checkout,topayment, func, insta
from django.contrib.admin import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home),
    url(r'^signin/$',sign_in),
    url(r'^login/$',log),
    url(r'^signup/$',sign_up),
    url(r'^product/(?P<id>\d+)/',prod),
    url(r'^addcart/(?P<id>\d+)/',addtocart),
    url(r'^updatecart/change/(?P<id>\d+)/',updatecart),
    url(r'^cart/',cartlist),
    url(r'^blogs/',blog),
    url(r'^faqs/',faqs),
    url(r'^dealer_contact/',dealer_cont),
    url(r'^customer_contact/',customer_cont),
    url(r'^seller_contact/',seller_cont),
    url(r'^submit_query/',sub_query),
    url(r'^checkout/',func),
    url(r'^checkout1/',insta),
    url(r'^topayment/',topayment),
    # url(r'^test/',test),
    url(r'^welcome/',welcome),
    url(r'^buy/',func),
    url(r'^forgot_password/',forgotpass),
]


















admin.site.site_header = "XYZ HERBAL PRODUCTS"
# AdminSite.site_title = "check it"
# admin.site.site_url = "http://www.google.com/" - to change the link to "view site" option


if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    

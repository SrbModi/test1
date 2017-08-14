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
<<<<<<< Updated upstream
from adminpanel.views import home,blog,faqs,prod,sub_query,dealer_cont,customer_cont,seller_cont,sub_query,welcome, aboutus,contact_cust,contact_dealer,contact_seller
from orders.views import addtocart,cartlist,updatecart,checkout,topayment, func, thankyou
=======
from adminpanel.views import home,blog,faqs,prod,sub_query,dealer_cont,customer_cont,seller_cont,sub_query,welcome
from orders.views import addtocart,cartlist,updatecart,checkout,topayment, func
>>>>>>> Stashed changes
from django.contrib.admin import *
from django.views.generic.base import  RedirectView
# import django.views.defaults

urlpatterns = [

    # ('^404testing/$', direct_to_template, {'template': '404.html'})
    url(r'^admin/', admin.site.urls),
    url(r'^$',home),
    url(r'^aboutus/$',aboutus),
    url(r'^signin/$',sign_in),
    url(r'^login/$',log),
    url(r'^signup/$',sign_up),
    url(r'^product/(?P<id>\d+)/',prod),
    url(r'^addcart/(?P<id>\d+)/',addtocart),
    url(r'^updatecart/change/(?P<id>\d+)/',updatecart),
    url(r'^cart/',cartlist),
    url(r'^blogs/',blog),
    url(r'^faqs/',faqs),
    url(r'^contact_cust/',contact_cust),
    url(r'^contact_dealer/',contact_dealer),
    url(r'^contact_seller/',contact_seller),
    url(r'^submit_query/',sub_query),
    url(r'^checkout/',func),
    url(r'^topayment/',topayment),
    # url(r'^test/',test),
    url(r'^welcome/',welcome),
    url(r'^buy/',func),
    url(r'^forgot_password/',forgotpass),
    # url(r'^forgot_password/em/',forgotpass),
    url(r'^otp/em/',accept_otp),
    url(r'^reset_password/',reset_pass),
    url(r'^thankyou/',thankyou),

    # url(r'^404/$', django.views.defaults.page_not_found),
]



# handler404 = 'handler'


admin.site.site_header = "MEDIFUDO"
# AdminSite.site_title = "check it"
# admin.site.site_url = "http://srb1403.pythonanywhere.com/" - to change the link to "view site" option
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

<<<<<<< Updated upstream
# urlpatterns += [url(r'^.*$', RedirectView.as_view(url='/',permanent=False),name='index'),]
=======

>>>>>>> Stashed changes

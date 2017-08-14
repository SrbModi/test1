from django.contrib import admin
from .models import cart,order_content,order_delivery
# Register your models here.

class cartadmin(admin.ModelAdmin):
	list_display = ["user","contact","email","prod_name","prod_id","qty"]

class order_contentadmin(admin.ModelAdmin):
	list_display = ["user","prod_name","prod_id","price","qty","offer"]

class order_deliveryadmin(admin.ModelAdmin):
	list_display = ["user","contact","address","landmark","city","state","pincode"]



admin.site.register(cart,cartadmin)
admin.site.register(order_content,order_contentadmin)
admin.site.register(order_delivery,order_deliveryadmin)
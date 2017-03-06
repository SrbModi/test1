from django.contrib import admin
# from django.contrib.admin import AdminSite
# from django.utils.translation import ugettext_lazy
from .models import *

# Register your models here.

class imageslideradmin(admin.ModelAdmin):
	list_display = ["image"]
	search_fields = ["=image"]

class productsadmin(admin.ModelAdmin):
	list_display = ["section","prod_name","prod_id","desc","price","offer","detail_desc","avail"]
	# fields = ["section","prod_name"]
	list_display_links = ["section","prod_name","prod_id","desc","price","offer","detail_desc","avail"]
	search_fields = ["=section","=prod_name","=prod_id","=price","=offer","=avail"]
	list_per_page = 100

class blogsadmin(admin.ModelAdmin):
	list_display = ["sub_by","sub_on","topic","matter"]
	#fields = ["sub_by","topic","matter"]
	list_filter = ["sub_by"]
	list_display_links = ["sub_by","sub_on","topic","matter"]
	search_fields = ["=sub_by","=sub_on","=topic","=matter"]
	#list_editable = ["sub_by"]
	list_per_page = 100
	ordering = ["sub_by","sub_on"]
	save_as = True

# class MyAdminSite(AdminSite):
# 	site_title = ugettext_lazy('My site admin')
# 	site_header = ugettext_lazy('My administration')


class eventsadmin(admin.ModelAdmin):
	list_display = ["name","desc","venue","date","time"]
	list_display_links = ["name","desc","venue","date","time"]
	search_fields = ["=name","=desc","=venue","=date","=time"]
	ordering = ["name","desc","venue","date","time"]

class faqadmin(admin.ModelAdmin):
	list_display = ["ques","ans"]
	list_display_links = ["ques","ans"]
	search_fields = ["=ques","=ans"]
	ordering = ["ques","ans"]

class othersadmin(admin.ModelAdmin):
	list_display = ["title","content"]
	list_display_links = ["title","content"]
	search_fields = ["=title","=content"]
	ordering = ["title","content"]

class enquiryadmin(admin.ModelAdmin):
	list_display = ["name","contact","email","city","state","subject","message"]
	list_display_links = ["name","contact","email","city","state","subject","message"]
	search_fields = ["=name","=contact","=email","=city","=state","=subject","=message"]
	ordering = ["name","contact","email","city","state","subject","message"]


admin.site.register(imageslider,imageslideradmin)
admin.site.register(products,productsadmin)
admin.site.register(blogs,blogsadmin)
admin.site.register(events,eventsadmin)
admin.site.register(faq,faqadmin)
admin.site.register(others,othersadmin)
admin.site.register(enquiry,enquiryadmin)
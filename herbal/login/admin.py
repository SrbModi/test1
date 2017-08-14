from django.contrib import admin

# Register your models here.
from .models import *

class loginadmin(admin.ModelAdmin):
	list_display = ["user","password","contact","email","address","status"]

admin.site.register(login_data,loginadmin)
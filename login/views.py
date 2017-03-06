from django.shortcuts import render
from django.db import models
from .models import *

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import login,logout
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


@csrf_exempt
def sign_in(request):
	if request.user.is_authenticated():
		print("user already logged in")
		return HttpResponseRedirect('/')
	else:
		if(request.POST == {}):
			print("null")
			return render(request,"login.html",{})

		print("Past the checks!!")
		response = {}
		# try:
		if request.method == "POST":
			username = str(request.POST.get("username"))
			password = str(request.POST.get("password"))
			print("username and password received.")
			if login_data.objects.filter(user=username).filter(password=password):
				user = authenticate(username=username,password=password)
				print(str(username)+" - user is authenticated")
				if user is not None:
					print("user is logging in...")
					login(request,user)
					print("user logged in")
					print(str(username) + " - user is logged in")
					return HttpResponseRedirect('/')
			else:
				print("username and password mismatch")
				return render(request,"login.html",{"message":"Username and Password do not match ! Please Try Again."})
	# except:
		# 	print("server side error!!!!!")
		# 	return render(request,"login.html",{"message":"server side issue"})


def log(request):
	if request.user.is_authenticated():
		logout(request)
		return HttpResponseRedirect('/')
	else:
		return render(request,"login.html",{})

@csrf_exempt
def sign_up(request):
	print(request.POST)
	if request.POST == {} : 
		print("null data")
		return render(request,"signup.html",{})
	# else:
	# try:
	username = request.POST.get("username")
	password = request.POST.get("password")
	contact = request.POST.get("contact")
	email = request.POST.get("email")
	add = request.POST.get("address")
	login_data.objects.create(user = username,
		password = password,
		contact = contact,
		email = email,
		address = add,
		status = 0)
	User.objects.create_user(
		username = username,
		password = password,
		email = email)
	return HttpResponseRedirect('/')
	# except:
	# 	print("Please fill all the fields")
	# 	return render(request,"signup.html",{"message":"Please fill all the fields."})


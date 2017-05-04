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
import random
from django.core.mail import send_mail


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

@csrf_exempt
def forgotpass(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		response={}
		context={}
		if request.method=="POST":
			response["success"]=True
			email=str(request.POST.get("email"))
			response["email"]=email
			try:
				user_row=login_data.objects.get(email=email)
				user = user_row.user
				print("1")
				response["message"]="email id found"
				context["message"]="Enter the otp sent to your email id"
				print("2")
			except:
				print("Unregistered Email adress entered for OTP")
				context["message"] = "This E-Mail Adress is not registered."
				return render(request,"forgot-password.html",context)

			otp=str(random.randint(1000,9999))
			msg = """
			Hello %s.
			The One time code for changing password to your Medifudo.com account is as under
			%s

			Team Medifudo.

			For any queries, contact 1800-121-2200 or drop us an email at help@medifudo.com

			Note: This is an auto-generated email. Please do not reply back to it.
			"""
			print (str(otp))
			setattr(user_row,'otp',int(otp))
			user_row.save()
			print("3")
			send_mail(
				"One-Time Code for MediFudo",
				msg %(user,otp),
				'sourabhrocks14@gmail.com',
				[str(email)],
				fail_silently=False,
				)
			print("4")
			context["email"] = request.POST.get("email")
			return render(request,"otp.html",context)
			# return HttpResponseRedirect('/otp/em/')
		else:
			print("sourabh")
			return render(request,"forgot-password.html")


@csrf_exempt
def accept_otp(request):
	context = {}
	mail = request.POST.get("email")
	print(mail)
	context["email"] = mail
	obj = login_data.objects.get(email=str(mail))
	print(obj)
	otp_object = int(obj.otp)
	otp_input = int(request.POST.get("otp"))
	print(otp_object)
	print(otp_input)
	if otp_object == otp_input:
		print("A")
		return render(request,"reset_pass.html",context)
	else:
		context["message"] = "Please Enter the Correct OTP"
		return render(request,"otp.html",context)

@csrf_exempt
def reset_pass(request):
    # context = {}
	print("loop :: reset_pass")
	mail = str(request.POST.get("email"))
	new_pass = str(request.POST.get("new_password"))
	print("1")
	if new_pass == str(request.POST.get("new_password1")):
		print("2")
		obj1 = login_data.objects.get(email = mail)
		obj2 = User.objects.get(email = mail)
		print("3")
		setattr(obj1,'password',new_pass)
		print("4")
		obj2.set_password(new_pass)
		print("5")
		obj1.save()
		obj2.save()
		print("password changed")
		return HttpResponseRedirect("/login/")

	else:
		print("6")
		context = {}
		context["message"] = "The password do not match."
		context["email"] = mail
		print("7")
		return render(request,"reset_pass.html",context)
	print("8")
	return HttpResponse("DOne")



def handler(request):
    #create some variables here if you like
    path = request.path
    response = render_to_response('404.html', locals(),
                              context_instance=RequestContext(request))
    response.status_code = 404
    return (response)
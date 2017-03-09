from django.shortcuts import render
from .models import imageslider,products,blogs, events, faq, others, enquiry
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import login,logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required




# Create your views here.

# submit button actions

#home page

url = "http://127.0.0.1:8000/"

def home(request):
	if request.user.is_authenticated():
		status = 'LOG OUT'
	else:
		status = 'LOG IN'
	str1 = ' '
	count = 0
	for o in imageslider.objects.all():
		print(o.image.url)
		if count == 0:
			str1 += '<div class="item active"><img src="'
		else:
			str1 += '<div class="item "><img src="'
		str1 += str(o.image.url)
		str1 += '"></div>'
		count += 1
	A = str1
	print(A)


	#section = pickel
	count = 0
	str1 = '<div class="item active"><div class="row-fluid"><div class="col-xs-1"></div>'
	for o in products.objects.filter(section="pickel"):
		count += 1
		str1 += '<div class="col-xs-2"><a href="#x" class="thumbnail"><img src="'
		str1 += str(o.image.url)
		str1 += '" alt="Image" style="max-width:100%;"></a>'
		str1 += '<div><div class="text-center"><a class = "text-uppercase" style="text-decoration:none; color:black; font-size:18px;" href="'
		str1 += url + 'product/' + str(o.prod_id) + '/'
		str1 += '">'
		str1 += str(o.prod_name)
		str1 +='</a><br><br><p class="text-uppercase" style="font-size:12px;">'
		str1 += str(o.short_desc)
		str1 += '</p></div><div class="text-center" style="font-size:18px; border-top: dashed 1px; border-bottom: dashed 1px;padding-top:5%;">'
		str1 += '<p>'
		if o.offer == 0:
			str1 += '<span style="color:black;margin:2%;font-size:19px">'
			str1 += '₹' + str(o.price)
			str1 += '</span><br>'
		else:
			str1 += '<span style="text-decoration:line-through; color:grey;margin:2%;font-size:19px">'
			price = o.price
			str1 += '₹' + str(price)
			str1 += '</span><span style="color:red;margin-left:0.1%;margin-right:4%;font-size:14px">'
			offer = o.offer
			str1 += str(offer) + '%' + ' off'
			str1 += '</span><br><span style="font-weight:bold; font-size:19px;margin:2%;">'
			rate = float(price-(price*offer/100))
			rate = round(rate,2)
			str1 += '₹' + str(rate)
			str1 += '</span></p>'
		str1 += '</div></div></div>'
		if count%5 == 0:
			str1 += '<div class="col-xs-1"></div></div></div>'
			str1 += '<div class="item "><div class="row-fluid"><div class="col-xs-1"></div>'

	if count%5 == 0:
		str1 = str1[:-70] #removing 70 characters from the end of str1 (from statement P)
	else:
		str1 += '<div class="col-xs-1"></div></div></div>'

	B = str1


	#section = amla
	count = 0
	str1 = '<div class="item active"><div class="row-fluid"><div class="col-xs-1"></div>'
	for o in products.objects.filter(section="amla"):
		count += 1
		str1 += '<div class="col-xs-2"><a href="#x" class="thumbnail"><img src="'
		str1 += str(o.image.url)
		str1 += '" alt="Image" style="max-width:100%;"></a>'
		str1 += '<div><div class="text-center"><a class = "text-uppercase" style="text-decoration:none; color:black; font-size:18px;" href="'
		str1 += url + 'product/' + str(o.prod_id) + '/'
		str1 += '">'
		str1 += str(o.prod_name)
		str1 +='</a><br><br><p class="text-uppercase" style="font-size:12px;">'
		str1 += str(o.short_desc)
		str1 += '</p></div><div class="text-center" style="font-size:18px; border-top: dashed 1px; border-bottom: dashed 1px;padding-top:5%;">'
		str1 += '<p>'
		if o.offer == 0:
			str1 += '<span style="color:black;margin:2%;font-size:19px">'
			str1 += '₹' + str(o.price)
			str1 += '</span>'
		else:
			str1 += '<span style="text-decoration:line-through; color:grey;margin:2%;font-size:19px">'
			price = o.price
			str1 += '₹' + str(price)
			str1 += '</span><span style="color:red;margin-left:0.1%;margin-right:4%;font-size:14px">'
			offer = o.offer
			str1 += str(offer) + '%' +' off'
			str1 += '</span><br><span style="font-weight:bold; font-size:19px;margin:2%;">'
			rate = float(price-(price*offer/100))
			rate = round(rate,2)
			str1 += '₹' + str(rate)
			str1 += '</span></p>'
		str1 += '</div></div></div>'
		if count%5 == 0:
			str1 += '<div class="col-xs-1"></div></div></div>'
			str1 += '<div class="item "><div class="row-fluid"><div class="col-xs-1"></div>'
		
	if count%5 == 0:
		str1 = str1[:-70] #removing 70 characters from the end of str1 (from statement P)
	else:
		str1 += '<div class="col-xs-1"></div></div></div>'

	C = str1

	return render(request,"index.html",{"slider":A,"pickel":B,"amla":C,"status":status})



#FAQs Page
def faqs(request):
	if request.user.is_authenticated():
		status = 'LOG OUT'
	else:
		status = 'LOG IN'
	str1 = ' '
	x = 1
	for o in faq.objects.all():
		str1 += '<div class="panel panel-default"><div class="panel-heading"><h4 class="panel-title"><a class='
		str1 += '"accordion-toggle collapsed" data-toggle="collapse" data-parent="#accordion" href="#collapse'
		str1 += str(x)
		str1 += '">'
		str1 += str(o.ques)
		str1 += '</a></h4></div><div id="collapse'
		str1 += str(x)
		str1 += '" class="panel-collapse collapse"><div class="panel-body">'
		str1 += str(o.ans)
		str1 += '</div></div></div>'
		x += 1

	return render(request,"faq.html",{"data":str1,"status":status})

# Blogs Page
def blog(request):
	if request.user.is_authenticated():
		status = 'LOG OUT'
	else:
		status = 'LOG IN'
	str1 = ' ' 
	x = 1
	for o in blogs.objects.all():
		str1 += '<div class="panel panel-default"><div class="panel-heading"><img class="blog-img panel-title" src="'
		str1 += str(o.image.url)
		str1 += '"></img><h3>'
		str1 += str(o.topic)
		str1 += '</h3><h5 >'
		str1 += str(o.sub_on)
		str1 = str1[:-13]
		str1 += '<button type="button" class="accordion-toggle collapsed btn btn-success btn-lg"data-toggle='
		str1 += '"collapse" data-parent="#accordion" href="#collapse'
		str1 += str(x)
		str1 += '"style="margin-left:80%;">Read</button></h5>'
		str1 += '</div><div id="collapse'
		str1 += str(x)
		str1 += '" class="panel-collapse collapse "><div class="panel-body">'
		str1 += str(o.matter)
		str1 += '</div></div></div>'
		x += 1

	return render(request,"blog.html",{"data":str1,"status":status})


def prod(request,id):
	context = {}
	if request.user.is_authenticated():
		context["status"] = 'LOG OUT'
	else:
		context["status"] = 'LOG IN'

	o = products.objects.get(prod_id=id)
	
	context["prod_id"] = id
	context["prod_name"] = o.prod_name
	context["image"] = o.image.url
	print(o.image.url)
	price = o.price
	offer = o.offer
	context["price"] = price
	context["offer"] = str(offer)
	amount = float(price - (price*offer/100))
	amount = round(amount,2)
	context["amount"] = amount
	
	if o.avail is True:
		context["avail"] = "available"
	else:
		context["avail"] = "not available"

	context["desc"] = o.desc
	context["nutrient_1"] = o.nut_1
	context["nutrient_2"] = o.nut_2
	context["nutrient_3"] = o.nut_3
	context["nutrient_4"] = o.nut_4
	context["nutrient_5"] = o.nut_5

	return render(request,"product.html",context)


def dealer_cont(request):
	context = {}
	if request.user.is_authenticated():
		context["status"] = 'LOG OUT'
	else:
		context["status"] = 'LOG IN'
	return render(request,"contact_dealer.html",context)

def customer_cont(request):
	context = {}
	if request.user.is_authenticated():
		context["status"] = 'LOG OUT'
	else:
		context["status"] = 'LOG IN'
	return render(request,"contact_dealer.html",context)

def seller_cont(request):
	context = {}
	if request.user.is_authenticated():
		context["status"] = 'LOG OUT'
	else:
		context["status"] = 'LOG IN'
	return render(request,"contact_dealer.html",context)


@csrf_exempt
def sub_query(request):
	enquiry.objects.create(
		name = request.POST.get("name"),
		email = request.POST.get("email"),
		contact = request.POST.get("contact"),
		city = request.POST.get("city"),
		state = request.POST.get("state"),
		subject = request.POST.get("subject"),
		message = request.POST.get("message"),
		)

	context["message"] = "Query Received"
	return HttpResponseRedirect('/dealer_contact/')


@csrf_exempt
def welcome(request):
	print(request.POST)
	return render(request,"welcome.html",{})
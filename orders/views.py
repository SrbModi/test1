from django.shortcuts import render
from .models import *
from login.models import login_data
from adminpanel.models import products
import hashlib
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.views import login,logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from hashlib import sha512
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from uuid import uuid4
from uuid import UUID
import uuid
<<<<<<< Updated upstream
# from instamojo_wrapper import Instamojo
=======
#from instamojo_wrapper import Instamojo
>>>>>>> Stashed changes
# from .util import generate_hash

# Create your views here.

qty_global = 0



@csrf_exempt
def addtocart(request,id):
	if request.user.is_authenticated():
		user = request.user.username
		obj1 = login_data.objects.get(user = user)

		if cart.objects.filter(user=user).filter(prod_id=id):
			obj2 = cart.objects.get(prod_id = id,user=user)
			obj2.qty += int(request.POST.get("qty"))
			obj2.save()
		else:
			obj2 = products.objects.get(prod_id = id)
			cart.objects.create(user = user,
				contact = obj1.contact,
				email = obj1.email,
				prod_name = obj2.prod_name,
				prod_id = obj2.prod_id,
				price = obj2.price,
				image = obj2.image.url,
				qty = request.POST.get("qty")
				)
		str1 = '/product/' + str(id) + '/'


		return HttpResponseRedirect(str1,{'message':'prdocut added to cart !'})
	else:
		return HttpResponseRedirect('/signin/')



def cartlist(request):
	if request.user.is_authenticated():
		str1 = ' '
		total = 0

		user = request.user.username
		for obj1 in cart.objects.filter(user=user):
			obj2 = products.objects.get(prod_id = obj1.prod_id)

			str1 +='<form  method="POST" action="http://srb1403.pythonanywhere.com/updatecart/change/'
			str1 += str(obj1.prod_id) + '/"><td>'

			str1 += '<tr><td><img src="'
			str1 += str(obj2.image.url)
			str1 += '" style="width:100px; height:100px; margin-left:20%;" ></td><td>'
			str1 += str(obj2.prod_name)
			str1 += '</td><td>'
			str1 += str(obj2.price)
			price = float(obj2.price)
			price = round(price,2)
			str1 += '</td><td>'

			str1 += str(obj2.offer) + '%'
			disc = float(price*obj2.offer/100)
			disc = round(disc,2)
			print(disc)
			str1 += '</td><td>'
			rate = float(obj2.price-disc)
			rate = round(rate,2)
			str1 += str(rate)
			str1 += '</td><td>'
			str1 += '<input type="number" id="quantity" class="form-control"  min="1" style="width:70px;"'
			str1 += ' value="'
			str1 += str(obj1.qty)
			qty = int(obj1.qty)
			str1 += '" name="qty"></td>'

			print(request.POST.get("qty"))
			print(qty_global)
			# qty = 1
			# print('quantity = '+qty)
			pricenew = (rate)*qty
			pricenew = round(pricenew,2)
			total += pricenew
			print(total)
			str1 +='<td id="total"> '
			str1 += str(pricenew)
			str1 += '</td><td>'
			str1 +='<button type="submit" class = "btn btn-success" >UPDATE</button></td></tr>' #intake quantity change
			str1 += '</form>'
		x = str1

		str1 = ' '

		amount_total = round(total,2)
		shipping_total = shipping_charge()  #----  define a function for shipping charges
		grand_total = amount_total + shipping_total
		print (grandtotal(user))
		return render(request,"cart.html",{"data":x,"a_total":amount_total,
			"s_total":shipping_total,"g_total":grand_total})
	else:
		return HttpResponseRedirect('/signin/')


@csrf_exempt
def change_qty(request):
	qty_global = request.POST.get("qty")
	print(qty_global)
	return HttpResponseRedirect('/cart/')

@csrf_exempt
def updatecart(request,id):
	user = request.user.username
	obj1 = cart.objects.get(user=user,prod_id=id)
	print(obj1.qty)
	obj1.qty = request.POST.get("qty")
	print(obj1.qty)
	obj1.save()
	return HttpResponseRedirect('/cart/')

def totalamt(user):
	total = float(0)

	for o in cart.objects.all():
		if o.user == user :
			temp = products.objects.get(prod_id = o.prod_id )
			price = o.price
			offer = temp.offer
			rate = price - (price*offer/100)
			print("rate = " + str(rate))
			total += float(rate*o.qty)
			total = round(total,2)

	return total

def shipping_charge():
	return (250)

def grandtotal(user):
	return totalamt(user) + shipping_charge()

def checkout(request):
	context = {}
	context["user"] = request.user.username
	obj = login_data.objects.get(user=request.user.username)
	context["email"] = obj.email
	context["contact"] = obj.contact
	context["address"] = obj.address
	return render(request,"checkout.html",context)


def topayment(request):
	order_delivery.objects.create(
		user = request.POST.get("user"),
		#order_id = request.POST.get("user"),
		email = request.POST.get("email"),
		address = request.POST.get("address"),
		landmark = request.POST.get("landmark"),
		city = request.POST.get("city"),
		state = request.POST.get("state"),
		pincode = request.POST.get("pincode")
		)
	return render(request,"checkout.html",{})

# def test1(request):
# 	MERCHANT_KEY = "gtKFFx"
# 	key="gtKFFx"
# 	SALT = "eCwWELxi"
# 	PAYU_BASE_URL = "https://test.payu.in/_payment"
# 	action = ''
# 	posted={}
# 	for i in request.POST:
# 		posted[i]=request.POST[i]
# 		hash_object = hashlib.sha256(b'randint(0,20)')
# 		txnid=hash_object.hexdigest()[0:20]
# 		hashh = ''
# 		posted['txnid']=txnid
# 		hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
# 		posted['key']=key
# 		hash_string=''
# 		hashVarsSeq = ''
# 		hashVarsSeq=hashSequence.split('|')
# 	for i in hashVarsSeq:
# 		try:
# 			hash_string+=str(posted[i])
# 		except Exception:
# 			hash_string+=''
# 			hash_string+='|'
# 			hash_string+=SALT
# 	hashh=hashlib.sha512(hash_string).hexdigest().lower()
# 	action =PAYU_BASE_URL
# 	if(posted.get("key")!=None and posted.get("txnid")!=None and posted.get("productinfo")!=None and posted.get("firstname")!=None and posted.get("email")!=None):
# 		return render_to_response('welcome.html',RequestContext(request,{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"https://test.payu.in/_payment" }))
# 	else:
# 		return render_to_response('welcome.html',RequestContext(request,{"posted":posted,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"." }))


# def test(request):
# 	key="gtKFFx"
# 	txnid = "abc123"
# 	amount = 100.00
# 	productinfo = "test product"
# 	firstname = "sourabh"
# 	email = "sourabh.modi14@gmail.com"
# 	phone = "9039189251"
# 	SALT = "eCwWELxi"
# 	surl = "http://127.0.0.1:8000/welcome/"
# 	furl = "http://www.google.com/"
# 	hashgen = ''
# 	hashgen= sha512(key|txnid|amount|productinfo|firstname|email|||||||||||SALT)

# 	PAYU_BASE_URL = "https://test.payu.in/_payment"
# 	POST_DATA = [('key','')]

# 	return HttpResponse("<h1>DONE</h1>")


###########################-----action on proceed to checkout-----###########################


def func(request):
	context = {}
	username = request.user.username
	obj1 = login_data.objects.get(user = username)
	context["user"] = username
# 	context["key"] = "gtKFFx"
# 	context["SALT"] = "eCwWELxi"
	context["productinfo"] = "product"
	context["firstname"] = username
# 	context["surl"] = "http://srb1403.pythonanywhere.com/"
# 	context["furl"] = "http://srb1403.pythonanywhere.com/"
# 	context["curl"] = "http://srb1403.pythonanywhere.com/"
	txnid = str(uuid.uuid1().int >> 64)
	context["txnid"] = txnid
	amount = grandtotal(username)
	amount = round(amount,2)
	context["amount"] = amount
	email = str(obj1.email)
	context["email"] = email
	context["phone"] = obj1.contact
# 	cleaned_data = {'key': settings.PAYU_INFO['merchant_key'], 'txnid': txnid,'amount': amount, 'productinfo': 'product','firstname': username, 'email':email, 'udf1': '', 'udf2': '', 'udf3': '', 'udf4': '', 'udf5': '', 'udf6': '','udf7': '',  'udf8': '', 'udf9': '', 'udf10': ''}
# 	context["hash_o"] = generate_hash(cleaned_data)

	return render(request,"checkout.html",context)
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes




###########################-----HASH GENERATION PAYEMNT GATEWAY-----###########################

# KEYS = ('key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
#         'udf1', 'udf2', 'udf3', 'udf4', 'udf5',  'udf6',  'udf7', 'udf8',
#         'udf9',  'udf10')


# def generate_hash(data):
#     # keys = ('key', 'txnid', 'amount', 'productinfo', 'firstname', 'email','eCwWELxi')
#     # hash = sha512(''.encode('utf-8'))
#     # for key in KEYS: #key or keys - get it confirmed
#     #     hash.update("%s%s" % (str(data.get(key, '')).encode('utf-8'), '|'))
#     d = ''
#     for key in KEYS:
#     	d += "%s%s" % (str(data.get(key)),'|')
#     print(d)
#     print ("new")
#     hash = sha512(d.encode('utf-8'))
#     # hash.update(d.encode('utf-8'))
#     hash.update(settings.PAYU_INFO.get('merchant_salt').encode('utf-8'))
#     print (hash)
#     return hash.hexdigest().lower()


# def verify_hash(data, SALT):
#     keys.reverse()
#     hash = sha512(settings.PAYU_INFO.get('merchant_salt'))
#     hash.update("%s%s" % ('|', str(data.get('status', ''))))
#     for key in KEYS:
#         hash.update("%s%s" % ('|', str(data.get(key, ''))))
#     return (hash.hexdigest().lower() == data.get('hash'))




# hash_o = hash_o.encode('utf-8')
	# data = """<html>
	#                       <head><title>Redirecting...</title></head>
	#                       <body>
	#                       <form action='%s' method='post' name="payu">
	#                           <input type="hidden" name="firstname" value="%s" />
	#                           <input type="hidden" name="surl" value="%s" />
	#                           <input type="hidden" name="phone" value="%s" />
	#                           <input type="hidden" name="key" value="%s" />
	#                           <input type="hidden" name="hash" value ="%s" />
	#                           <input type="hidden" name="curl" value="%s" />
	#                           <input type="hidden" name="furl" value="%s" />
	#                           <input type="hidden" name="txnid" value="%s" />
	#                           <input type="hidden" name="productinfo" value="%s" />
	#                           <input type="hidden" name="amount" value="%s" />
	#                           <input type="hidden" name="email" value="%s" />
	#                           <input type="hidden" value="submit">
	#                       </form>
	#                       </body>
	#                       <script language='javascript'>
	#                       window.onload = function(){
	#                        document.forms['payu'].submit()
	#                       }
	#                       </script>
	#                   </html>
 #    """ % (settings.PAYU_INFO['payment_url'],
 #    	name,
 #    	settings.PAYU_INFO['surl'],
 #    	9039189251,
 #    	settings.PAYU_INFO['merchant_key'],
 #    	hash_o,settings.PAYU_INFO['curl'],
 #    	settings.PAYU_INFO['furl'],
 #    	txnid,
 #    	product_title,
 #    	amount,
 #    	email
 #    	)

	# return HttpResponse("hello")

###########################-----REDIRECT FROM CHECKOUT TO THANK YOU PAGE-----###########################

@csrf_exempt
def thankyou(request):
# 	try:
	username = request.POST.get("user")
	for o in cart.objects.filter(user=username):
		obj = products.objects.get(prod_id=o.prod_id)
		order_content.objects.create(
			user = username,
			prod_name = o.prod_name,
			prod_id = o.prod_id,
			price = o.price,
			qty = o.qty,
			offer = obj.offer
			)
	print("1");
	order_delivery.objects.create(
		user = request.POST.get("user"),
		email = request.POST.get("email"),
		address = request.POST.get("address"),
		landmark = request.POST.get("landmark"),
		city = request.POST.get("city"),
		state = request.POST.get("state"),
		pincode = request.POST.get("pincode")
		)

	msg = """Hello Admin.
	The  user - %s has placed an order. Please visit the admin panel and check the order under "Order Content" for order details and "Order Delivery" for details of delivery
	Contact details of user:
	Name : %s
	Contact : %s
	Email : %s
	city : %s

<<<<<<< Updated upstream

	Follow the link
	Order Contents : http://srb1403.pythonanywhere.com/admin/orders/order_content/
	Order Delivery : http://srb1403.pythonanywhere.com/admin/orders/order_delivery/


	Thank You. Have A great Day.
	"""
	send_mail(
			"New Order from MediFudo.com",
			msg %(username,username,request.POST.get("contact"),request.POST.get("email"),request.POST.get("city")),
			'sourabhrocks14@gmail.com',
			[str(email)],
			fail_silently=False,
			)

	context = {}
	context["message"] = "Thank You. You will soon be contacted by our representative."

	return render(request,"thankyou.html",context)
# 	except Exception as e:
# 	    print (str(e))
# 	    context = {}
# 	    context["message"] = "Sorry. We were unale to process your request due to some internal error.Please try again"
# 	    return render(request,"thankyou.html",context)
=======
# @csrf_exempt
# def insta(request):
# 	api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');
# 	response = api.payment_request_create(
# 		amount='3499',
#     	purpose='FIFA 16',
#     	send_email=True,
#     	email="sourabh.modi14@gmail.com",
#     	redirect_url="http://127.0.0.1:8000/"
#     	)
# 	# print the long URL of the payment request.
# 	print (response['payment_request']['longurl'])
# 	# print the unique ID(or payment request ID)
# 	print (response['payment_request']['id'])
# 	return HttpResponse("Check the terminal")
>>>>>>> Stashed changes

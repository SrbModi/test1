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

			str1 +='<form  method="POST" action="http://127.0.0.1:8000/updatecart/change/'
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
			temp = products.objects.get(prod_name = o.prod_name )
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


# def buy_order(request):
#     """ funtion for save all orders and genarate order id"""
#     items = None
#     orderitem = None
#     extra = False
#     if request.user.is_authenticated() and not request.user.is_staff:
#         user = request.user.username
#         # try:
#         #     cart = Cart.objects.get(buyer=request.user)
#         # except ObjectDoesNotExist:
#         #     extra = "You dont have any item in your cart"
#         #     variables = RequestContext(request, {'extra': extra})
#         #     return render_to_response('home.html', variables)
#             # total_amount = OrderItem.objects.filter(buyer=request.user)
#     item_list = []
#     # rg = request.POST.get
#     # if cart:
#     # if request.POST:
#     # rg('shippingnme')and rg('shippingaddress') and rg('shippingemail') and                                                   rg('shippingpostel') and rg('shippingcity') and rg('shippingcountry') and                                                 rg('shippingcountry') rg('shippingphone'):
#     # try:
#     """store all products to myorder model and genarate order id for the order"""
#     # myorder = MyOrder(buyer=user)
#     # billing User
#     # myorder.buyer = user
#     # myorder of Billing  Address
#     # myorder.billing_name = request.POST.get('billingname')
#     # myorder.billing_street_address = request.POST.get(
#     #     'billingaddress')
#     # myorder.billing_pincode = request.POST.get('billingpostel')
#     # myorder.billing_city = request.POST.get('billingcity')
#     # myorder.billing_country = request.POST.get('billingcountry')
#     # myorder.billing_state = request.POST.get('billingstate')
#     # myorder.billing_mobile = request.POST.get('billingphone')
#     # myorder.billing_email = request.POST.get('billingemail')

#     # myorder of shipping Address
#     # myorder.shipping_pincode = request.POST.get('shippingpostel')
#     # myorder.shipping_name = request.POST.get('shippingnme')
#     # myorder.shipping_street_address = request.POST.get(
#     #     'shippingaddress')
#     # myorder.shipping_city = request.POST.get('shippingcity')
#     # myorder.shipping_state = request.POST.get('shippingstate')
#     # myorder.shipping_mobile = request.POST.get('shippingphone')
#     # myorder.shipping_country = request.POST.get('shippingcountry')
#     # myorder.shipping_email = request.POST.get('shippingemail')
#     # if request.POST.get('paymentmethod'):
#     #     myorder.payment_method = request.POST.get('paymentmethod')
#     # else:
#     #     myorder.payment_method = 'ON'
#     # myorder.comment =  request.POST.get('prodcutmessage')

#     # print ("my messages ")
#     # print (myorder.comment)

#   # payment_method
#   # comment
#     # myorder.txnid = str(uuid.uuid1().int >> 64)
#     txnid = str(uuid.uuid1().int >> 64)
#     # myorder.save()
#     """genarate an order id, the below loop will add all ordered product to the                                               order"""

#     # for order in cart.items.all():
#     #     orderitem = OrderItem()
#     #     orderitem.buyer = order.buyer
#     #     orderitem.product_id = order.product.id
#     #     orderitem.product_title = order.product.name
#     #     orderitem.weight = order.product.weight
#     #     orderitem.product_price = order.product.gross_pay()[0]
#     #     orderitem.total_amount = order.total
#     #     orderitem.quantity = order.quantity
#     #     orderitem.save()
#     #     myorder.items.add(orderitem)
#     # total_details = total_price_fu(myorder)

#     """ After adding products to order assigning a
#     transaction amount and shipping charge to the order"""
#     # myorder = MyOrder.objects.get(pk=myorder.txnid)

#     # myorder.amount = total_details['grand_total']
#     amount = float(100,2)
#     # myorder.shipping_rate = total_details['shipping_rate']
#     name = 'sourabh'
#     product_title = 'amla01'
#     email = 'sourabh.modi14@gmail.com'

#     """Assigning all values for hash funtion for payu"""

#     cleaned_data = {'key': settings.PAYU_INFO['merchant_key'], 'txnid': txnid,'amount': amount, 'productinfo':product_title,'firstname': name, 'email':email, 'udf1': ' ', 'udf2': '', 'udf3': '', 'udf4': '', 'udf5': '', 'udf6': '','udf7': '',  'udf8': '', 'udf9': '', 'udf10': ''}

#     """ the generate_hash funtion is use for genarating hash
#      value from cleaned_data"""
#     hash_o = generate_hash(cleaned_data)
#     # myorder.hash =hash_o
#     # myorder.save()

    
#     data = """<html>
# 	                      <head><title>Redirecting...</title></head>
# 	                      <body>
# 	                      <form action='%s' method='post' name="payu">
# 	                          <input type="hidden" name="firstname" value="%s" />
# 	                          <input type="hidden" name="surl" value="%s" />
# 	                          <input type="hidden" name="phone" value="%s" />
# 	                          <input type="hidden" name="key" value="%s" />
# 	                          <input type="hidden" name="hash" value =
# 	                          "%s" />
# 	                          <input type="hidden" name="curl" value="%s" />
# 	                          <input type="hidden" name="furl" value="%s" />
# 	                          <input type="hidden" name="txnid" value="%s" />
# 	                          <input type="hidden" name="productinfo" value="%s" />
# 	                          <input type="hidden" name="amount" value="%s" />
# 	                          <input type="hidden" name="email" value="%s" />
# 	                          <input type="hidden" value="submit">
# 	                      </form>
# 	                      </body>
# 	                      <script language='javascript'>
# 	                      window.onload = function(){
# 	                       document.forms['payu'].submit()
# 	                      }
# 	                      </script>
# 	                  </html>
#     """ % (settings.PAYU_INFO['payment_url'],
#     	name, 
#     	settings.PAYU_INFO['surl'],v
#     	9039189251,
#     	settings.PAYU_INFO['merchant_key'],
#     	hash_o,settings.PAYU_INFO['curl'],
#     	settings.PAYU_INFO['furl'],
#     	txnid,
#     	product_title,
#     	amount,
#     	email
#     	)
	
# 	# data_str = str(data)
# 	return HttpResponse("<h1>Hello</h1>")

def func(request):
	context = {}
	username = request.user.username
	obj1 = login_data.objects.get(user = username)
	context["user"] = username
	context["key"] = "gtKFFx"
	context["SALT"] = "eCwWELxi"
	context["productinfo"] = "product"
	context["firstname"] = username
	context["surl"] = "http://127.0.0.1:8000/"
	context["furl"] = "http://127.0.0.1:8000/"
	context["curl"] = "http://127.0.0.1:8000/"
	txnid = str(uuid.uuid1().int >> 64)
	context["txnid"] = txnid
	amount = grandtotal(username)
	amount = round(amount,2)
	context["amount"] = amount
	email = str(obj1.email)
	context["email"] = email
	context["phone"] = obj1.contact
	cleaned_data = {'key': settings.PAYU_INFO['merchant_key'], 'txnid': txnid,'amount': amount, 'productinfo': 'product','firstname': username, 'email':email, 'udf1': '', 'udf2': '', 'udf3': '', 'udf4': '', 'udf5': '', 'udf6': '','udf7': '',  'udf8': '', 'udf9': '', 'udf10': ''}
	context["hash_o"] = generate_hash(cleaned_data)

	return render(request,"checkout.html",context)
	



###########################-----HASH GENERATION-----###########################

KEYS = ('key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
        'udf1', 'udf2', 'udf3', 'udf4', 'udf5',  'udf6',  'udf7', 'udf8',
        'udf9',  'udf10')


def generate_hash(data):
    # keys = ('key', 'txnid', 'amount', 'productinfo', 'firstname', 'email','eCwWELxi')
    # hash = sha512(''.encode('utf-8'))
    # for key in KEYS: #key or keys - get it confirmed
    #     hash.update("%s%s" % (str(data.get(key, '')).encode('utf-8'), '|'))
    d = ''
    for key in KEYS:
    	d += "%s%s" % (str(data.get(key)),'|')
    print(d)
    print ("new")
    hash = sha512(d.encode('utf-8'))
    # hash.update(d.encode('utf-8'))
    hash.update(settings.PAYU_INFO.get('merchant_salt').encode('utf-8'))
    print (hash)
    return hash.hexdigest().lower()


def verify_hash(data, SALT):
    keys.reverse()
    hash = sha512(settings.PAYU_INFO.get('merchant_salt'))
    hash.update("%s%s" % ('|', str(data.get('status', ''))))
    for key in KEYS:
        hash.update("%s%s" % ('|', str(data.get(key, ''))))
    return (hash.hexdigest().lower() == data.get('hash'))




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

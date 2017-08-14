from django.db import models

# Create your models here.

class cart(models.Model):
	user = models.CharField(max_length=50)
	contact = models.BigIntegerField(default=0000000000)
	email = models.CharField(max_length=100,null=True)
	prod_name = models.CharField(max_length=15)
	prod_id = models.IntegerField()
	price = models.PositiveIntegerField(null=True,blank=True)
	image = models.ImageField()
	qty = models.SmallIntegerField(default = 1)

class order_content(models.Model):
    user = models.CharField(max_length=50, default='user')
    prod_name = models.CharField(max_length=15)
    prod_id = models.IntegerField()
    price = models.PositiveIntegerField(null=True,blank=True)
    qty = models.SmallIntegerField(default = 1)
    offer = models.SmallIntegerField()


class order_delivery(models.Model):
	user = models.CharField(max_length=50)
	contact = models.BigIntegerField(default=0000000000)
	email = models.CharField(max_length=100,null=True,unique=True)
	address = models.CharField(max_length=256,null=True)
	landmark = models.CharField(max_length=256,null=True)
	city = models.CharField(max_length=256,null=True)
	state = models.CharField(max_length=256,null=True)
	pincode = models.SmallIntegerField(default=492010)


class MyOrder(models.Model):
    order_date = models.DateField(auto_now=True)
    txnid = models.CharField(max_length=36, primary_key=True)
    amount = models.FloatField(null=True, blank=True,default=0.0)
    hash = models.CharField(max_length=500, null=True, blank=True)
    billing_name = models.CharField(max_length=500, null=True, blank=True)
    billing_street_address = models.CharField(max_length=500, null=True, blank=True)
    billing_country = models.CharField(max_length=500, null=True, blank=True)
    billing_state = models.CharField(max_length=500, null=True, blank=True)
    billing_city = models.CharField(max_length=500, null=True, blank=True)
    billing_pincode = models.CharField(max_length=500, null=True, blank=True)
    billing_mobile = models.CharField(max_length=500, null=True, blank=True)
    billing_email = models.CharField(max_length=500, null=True, blank=True)

    shipping_name = models.CharField(max_length=500, null=True, blank=True)
    shipping_street_address = models.CharField(max_length=500, null=True, blank=True)
    shipping_country = models.CharField(max_length=500, null=True, blank=True)
    shipping_state = models.CharField(max_length=500, null=True, blank=True)
    shipping_city = models.CharField(max_length=500, null=True, blank=True)
    shipping_pincode = models.CharField(max_length=500, null=True, blank=True)
    shipping_mobile = models.CharField(max_length=500, null=True, blank=True)
    shipping_rate = models.FloatField(null=False, blank=False, default=0.0)
    status = models.CharField(max_length=500, null=True, blank=True)
    shipping_email = models.CharField(max_length=500, null=True, blank=True)

    payment_method = models.CharField(max_length=1000,verbose_name='Payment-method')
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)

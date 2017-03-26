from django.db import models

# Create your models here.


#cons = consult for constraints with the front-end 
#validation on fron-end???
class imageslider(models.Model):
	image = models.ImageField(null=True,blank=True)

class products(models.Model):
	section = models.CharField(max_length=256) #cons
	prod_name = models.CharField(max_length=25) #cons
	prod_id = models.IntegerField()
	short_desc = models.CharField(max_length=40,null = True)
	desc = models.TextField() #cons - any max_length required?
	price = models.PositiveIntegerField(null=True)
	image = models.ImageField(null = True)
	offer = models.SmallIntegerField()
	# detail_desc = models.TextField() #consult for ease of data entering #cons
	avail = models.BooleanField()
	Energy = models.CharField(max_length=12,default = 0)
	Fibre = models.CharField(max_length=12,default = 0)
	Fat = models.CharField(max_length=12,default = 0)
	Protein = models.CharField(max_length=12,default = 0)
	Vitamin_C = models.CharField(max_length=12,default = 0)
	Total_Carbohydrates = models.CharField(max_length=12,default = 0)
	Sugar = models.CharField(max_length=12,default = 0)
	Iron = models.CharField(max_length=12,default = 0)
	Calcium = models.CharField(max_length=12,default = 0)
	Calorific_value = models.CharField(max_length=12,default = 0)
	Crude_Fibre = models.CharField(max_length=12,default = 0)
	Sodium = models.CharField(max_length=12,default = 0)
	

class blogs(models.Model):
	sub_by = models.CharField(max_length=30) #cons
	sub_on = models.DateTimeField(auto_now_add=True) #cons - date+time
	topic = models.CharField(max_length=50) #cons
	matter = models.TextField()
	image = models.ImageField(null = True, blank=True)

class events(models.Model):
	name = models.CharField(max_length=256) #cons
	desc = models.TextField()
	image = models.ImageField(null=True,blank=True)
	venue = models.CharField(max_length=256)
	date = models.CharField(max_length=256)
	time = models.CharField(max_length=256)

class faq(models.Model):
	ques = models.CharField(max_length=256)
	ans = models.TextField()

#will need revision while implimenting
class others(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()

class enquiry(models.Model):
	name = models.CharField(max_length=256)
	email = models.EmailField(max_length=256)
	contact = models.BigIntegerField()
	city = models.CharField(max_length=256,null=True)
	state = models.CharField(max_length=256,null=True)
	subject = models.CharField(max_length=50,null=True)
	# ref = models.CharField(max_length=100)
	message = models.TextField()

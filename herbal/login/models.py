from django.db import models

# Create your models here.

class login_data(models.Model):
	user = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	contact = models.BigIntegerField(default=0000000000)
	email = models.CharField(max_length=100,null=True,unique=True)
	address = models.CharField(max_length=256,null=True)
	status = models.SmallIntegerField(default = '0',null=True)
	otp = models.SmallIntegerField(default = '0',null=True)

	#email-verification
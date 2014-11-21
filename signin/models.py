from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	
	uniqueid = models.CharField(max_length = 10)
	choices = models.CharField(max_length = 1500, default = "")
	pdstatus = models.CharField(max_length = 1,default = "N")
	category = models.CharField(max_length = 2 , default = "GE")
	locked = models.CharField(max_length = 1, default = "N")
		
	def __str__(self):
		return self.user.username+" "+self.choices

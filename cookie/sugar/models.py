from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Food(models.Model):
	name = models.CharField(max_length=200)
	
	#calories & shit


class UserProfile(models.Model):
	user = models.OneToOneField(User)
import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Food(models.Model):
	name = models.CharField(max_length=200)
	output = models.CharField(max_length=1000)
	last_day_served = models.DateTimeField()

	def days_since_served(self):
		return (timezone.now() - self.last_day_served).days

	def serving_today(self):
		return self.days_since_served() == 0

	def add_location(self, loc, time):
		if not self.serving_today():
			self.output = self.name + " will be served today "
			self.last_day_served = timezone.now()
		else:
			self.output += ", "
		self.output += "at " + loc + " for " + time

	def __str__(self):
		return self.name


class UserProfile(models.Model):
	user = models.OneToOneField(User)
	favs = models.CharField(max_length=1000)

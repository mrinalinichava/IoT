# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.

class user(models.Model):
	user_id = models.AutoField(primary_key=True)
	user_name = models.CharField(max_length=50, default="")
	firstname = models.CharField(max_length=50, default="")
	password = models.CharField(max_length=50)
	mobile_number = models.CharField(max_length=10)

	def __str__(self):
		return self.user_name


class vehicle(models.Model):
	vehicle_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey('user', to_field='user_id', on_delete=models.CASCADE)
	vehicle_name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.vehicle_name

class tracking(models.Model):
	vehicle_id = models.ForeignKey('vehicle', to_field='vehicle_id', on_delete=models.CASCADE)
	latitude = models.FloatField()
	longitude = models.FloatField()
	time = models.DateTimeField()




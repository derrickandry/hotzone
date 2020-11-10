from django.db import models

# Create your models here.
class Location(models.Model):
	location = models.CharField(max_length = 100)
	address = models.CharField(max_length = 200, default="", null=True, blank=True) 
	x_coor = models.DecimalField(max_digits = 50, decimal_places = 10)
	y_coor = models.DecimalField(max_digits = 50, decimal_places = 10)
	
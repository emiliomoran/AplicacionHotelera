from django.db import models

# Create your models here.

class Tour_Package(models.Model):

	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 250)
	company = models.CharField(max_length = 120)
	days = models.CharField(max_length = 150)
	hours = models.CharField(max_length = 100)
	price = models.IntegerField(default = 0)
	path_image = models.CharField(max_length= 250)


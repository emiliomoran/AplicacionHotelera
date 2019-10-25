from django.db import models

# Create your models here.

class Tour_Package(models.Model):

	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 250)
	price = models.IntegerField(default = 0)
	path_image = models.CharField(max_length= 250)


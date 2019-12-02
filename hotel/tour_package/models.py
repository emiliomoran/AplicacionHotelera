from django.db import models
from shopping_cart.models import Product
from accesos.models import Perfil
# Create your models here.

class Tour_Package(models.Model):
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 250)
	available_stock = models.IntegerField(default = 30)
	company = models.CharField(max_length = 120)
	days = models.CharField(max_length = 150)
	hours = models.CharField(max_length = 100)
	price = models.IntegerField(default = 0)
	path_image = models.FileField(max_length= 250)

	def __str__(self):
		return '{0} - {1}'.format(self.company,self.title)

class TourOrder(Product):

	tour = models.OneToOneField(Tour_Package, on_delete = models.SET_NULL, null = True)
	reservation_name = models.OneToOneField(Perfil,on_delete = models.SET_NULL, null = True)
	
from django.db import models

from reservas.models import Booking
from accesos.models import Perfil

# Create your models here.

class OrderItem(models.Model):
	reserva = models.OneToOneField(Booking, on_delete = models.SET_NULL, null = True)##Aqui debe cambiarse 
	#para que despues pueda ser habitacion, algun servicio, etc...
	is_ordered = models.BooleanField(default=False)
	date_added = models.DateTimeField(auto_now = True)
	date_ordered = models.DateTimeField(null=True)

	def __str__(self):
		return self.product

class Order(models.Model):

	reference_code = models.CharField(max_length = 12)
	owner = models.ForeignKey(Perfil,on_delete= models.SET_NULL,null=True)
	is_ordered = models.BooleanField(default = True)
	items = models.ManyToManyField(OrderItem)

	def get_items(self):
		return self.items.all()

	def get_cart_total(self):
		return sum([item.reserva.get_total_price(item.reserva) for item in self.items.all()])

	def __str__(self):
		return '{0} - {1}'.format(self.owner,self.reference_code)

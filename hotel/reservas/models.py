from django.db import models
from accesos.models import Perfil

# Create your models here.

class RoomType(models.Model):
	nombre = models.CharField(max_length = 150)	
	descripcion = models.CharField(max_length = 200)
	eliminado = models.BooleanField(default=False)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '%s. %s' % (self.id, self.nombre)

class Room(models.Model):
	id_roomtype = models.ForeignKey(RoomType, on_delete = models.CASCADE , verbose_name ="Tipo de Cuarto")
	descripcion = models.CharField(max_length = 200, verbose_name ="Descripcion del Cuarto")
	path_image = models.TextField(null=True, verbose_name="Url de Imagen")
	calificacion = models.IntegerField(default=0, verbose_name="Calificacion")
	num_camas = models.IntegerField(default=0, verbose_name="Numero de Camas")
	num_adultos = models.IntegerField(default=0, verbose_name="Numero de Adultos")
	num_ninos = models.IntegerField(default=0, verbose_name="Numero de Niños")
	precio = models.FloatField(default=0, verbose_name="Precio")
	disponible = models.BooleanField(default=True)		#True si esta disponible - False si esta reservada
	eliminado = models.BooleanField(default=False)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)


class BookingType(models.Model):
	name = models.CharField(max_length = 50)
	description = models.CharField(max_length = 150)
	is_removed = models.BooleanField(default = False)
	create_date = models.DateTimeField(auto_now_add = True)
	update_date = models.DateTimeField(auto_now = True)

class BookingState(models.Model):
	name = models.CharField(max_length = 50)
	description = models.CharField(max_length = 150)
	is_removed = models.BooleanField(default = False)
	create_date = models.DateTimeField(auto_now_add = True,  blank = True)
	update_date = models.DateTimeField(auto_now = True, blank = True)


class Booking(models.Model):
	customer_id = models.ForeignKey(Perfil, on_delete = models.CASCADE)
	room_id = models.ForeignKey(Room,on_delete = models.CASCADE)
	bookingtype_id = models.ForeignKey(BookingType, on_delete = models.CASCADE)
	state_id = models.ForeignKey(BookingState, on_delete = models.CASCADE)
	booking_date = models.DateTimeField(auto_now_add = True)
	check_in_date = models.DateTimeField(null= True)
	check_out_date = models.DateTimeField(null= True)
	no_nights = models.IntegerField(default = 0)
	is_removed = models.BooleanField(default = False)
	create_date = models.DateTimeField(auto_now_add = True)
	update_date = models.DateTimeField(auto_now = True)

	def get_total_price(self):

		room = Room.objects.filter(id=self.room_id).first()
		#Se debe implementar para que tambien sume el precio de los servicios despues agregados
		
		return room.precio


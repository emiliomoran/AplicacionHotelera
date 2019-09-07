from django.db import models

# Create your models here.

class RoomType(models.Model):
	nombre = models.CharField(max_length = 150)	
	descripcion = models.CharField(max_length = 200)
	eliminado = models.BooleanField(default=False)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)

	# def __str__(self):
	# 	return '%s %s' % (self.id, self.nombre)

class Room(models.Model):
	id_roomtype = models.ForeignKey(RoomType, on_delete = models.CASCADE)
	descripcion = models.CharField(max_length = 200)
	path_image = models.TextField(null=True)
	calificacion = models.IntegerField(default=0)
	num_camas = models.IntegerField(default=0)
	num_adultos = models.IntegerField(default=0)
	num_ninos = models.IntegerField(default=0)
	precio = models.FloatField(default=0)
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

class Booking_State(models.Model):
	name = models.CharField(max_length = 50)
	description = models.CharField(max_length = 150)
	is_removed = models.BooleanField(default = False)

	create_date = models.DateTimeField(auto_now_add = True)
	update_date = models.DateTimeField(auto_now = True)

	
class Booking(models.Model):
	customer_id = models.OneToOneField('accesos.Cliente', on_delete = models.CASCADE)
	room_id = models.OneToOneField(Room,on_delete = models.CASCADE)
	bookingtype_id = models.OneToOneField(BookingType, on_delete = models.CASCADE)
	state_id = models.ForeignKey(Booking_State, on_delete = models.CASCADE)

	booking_date = models.DateTimeField(auto_now_add = True)
	check_in_date = models.DateTimeField()
	check_out_date = models.DateTimeField()
	no_nights = models.IntegerField(default = 0)
	is_removed = models.BooleanField(default = False)

	create_date = models.DateTimeField(auto_now_add = True)
	update_date = models.DateTimeField(auto_now = True)


from django.db import models
from accesos.models import Cliente

# Create your models here.

class RoomType(models.Model):
	nombre = models.CharField(max_length = 150)
	tipo = models.IntegerField()	#0->suite - 1->familiar - 2->deluxe - 3->clasico
	descripcion = models.CharField(max_length = 200)
	estado = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)

class Room(models.Model):
	tipo_habitacion = models.OneToOneField(RoomType, on_delete = models.CASCADE)
	descripcion = models.CharField(max_length = 200)
	num_camas = models.IntegerField()
	precio = models.FloatField()
	disponible = models.BooleanField(default=True)		#True si esta disponible - False si esta reservada
	estado = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)

class Booking(models.Model):	
	reserva_inicio = models.DateTimeField()
	reserva_fin = models.DateTimeField()
	estaReservado = models.BooleanField()
	num_noches = models.IntegerField()
	activa = models.BooleanField(default=True)		#True si esta activa y False si no esta activa
	id_room = models.OneToOneField(Room, on_delete = models.CASCADE)
	id_cliente = models.OneToOneField(Cliente, on_delete = models.CASCADE)
	estado = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
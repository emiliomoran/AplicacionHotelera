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

# class Booking(models.Model):	
# 	reserva_inicio = models.DateTimeField()
# 	reserva_fin = models.DateTimeField()
# 	estaReservado = models.BooleanField()
# 	num_noches = models.IntegerField()
# 	activa = models.BooleanField(default=True)		#True si esta activa y False si no esta activa
# 	id_room = models.OneToOneField(Room, on_delete = models.CASCADE)
# 	id_cliente = models.OneToOneField(Cliente, on_delete = models.CASCADE)
# 	estado = models.BooleanField(default=True)
# 	fecha_creacion = models.DateTimeField(auto_now_add=True)
# 	fecha_modificacion = models.DateTimeField(auto_now=True)
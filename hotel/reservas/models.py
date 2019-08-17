from django.db import models

# Create your models here.

class RoomType(models.Model):

	nombre = models.CharField(max_length = 150)
	descripcion = models.CharField(max_length = 200)
	precio = models.FloatField()

class Room(models.Model):

	tipo_habitacion = models.OneToOneField(RoomType, on_delete = models.CASCADE)
	reserva_inicio = models.DateTimeField()
	reserva_fin = models.DateTimeField()
	estaReservado = models.BooleanField()

	def __str__(self):
		return self.tipo_habitacion.nombre




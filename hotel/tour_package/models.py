from django.db import models

# Create your models here.

class Tour_Package(models.Model):

	titulo = models.CharField(max_length = 100)
	descripcion = models.CharField(max_length = 250)
	precio = models.IntegerField(default = 0)


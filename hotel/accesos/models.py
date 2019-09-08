from django.db import models

# Create your models here.
from django.contrib.auth.models import UserManager
from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractBaseUser

class Cliente(AbstractBaseUser):
	nombres = models.CharField(max_length = 100)
	apellidos = models.CharField(max_length = 100)
	fecha_nacimiento = models.DateField(null=True)
	username = models.CharField(max_length = 100, unique=True, null=True)
	email = models.EmailField(unique=True)
	password = models.TextField()
	estado = models.BooleanField(default=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)

	USERNAME_FIELD = 'username'
	
	objects = UserManager()


class Perfil(models.Model):
	usuario = models.OneToOneField(Cliente,on_delete = models.CASCADE)
	#reservas = models.ManyToManyField(Booking, blank =  True) CREO QUE NO DEBERIA IR ACA

	def __str__(self):
		return '{0} {1}'.format(self.usuario.nombres,self.usuario.apellidos)


"""def post_save_profile_create(sender,instance,create,**kwargs):
	if created:
		Perfil.objects.create(usuario = instance)

post_save.connect(post_save_profile_create, sender = Cliente)    """
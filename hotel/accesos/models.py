from django.db import models
from administracion.choices import GENERO,TIPO_DE_IDENTIFICACION
# Create your models here.
from django.contrib.auth.models import UserManager
from django.db.models.signals import post_save

from django.contrib.auth.models import AbstractBaseUser
from tour_package.models import Tour_Package

class Usr(AbstractBaseUser):	
	username = models.CharField(max_length = 100, unique=True, null=True)
	email = models.EmailField(unique=True)
	password = models.TextField()
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	is_removed = models.BooleanField(default=False)
	create_date = models.DateTimeField(auto_now_add = True,  blank = True)
	update_date = models.DateTimeField(auto_now = True, blank = True)
	
	USERNAME_FIELD = 'username'
	objects = UserManager()

class Perfil(models.Model):
	doc_type = models.CharField(max_length = 9, choices = TIPO_DE_IDENTIFICACION, null=True)
	genero = models.CharField(max_length = 1, choices = GENERO, null=True)
	usr_id = models.OneToOneField(Usr, on_delete = models.CASCADE)
	name = models.CharField(max_length=100)
	cedula = models.CharField(max_length=15, unique = True, null=True)#ESTO NO SOLO PUEDE SER CEDULA, SINO MAS DOCUMENTOS
	last_name = models.CharField(max_length=100)
	phone = models.CharField(max_length=10, null=True)
	date_birth = models.DateField()
	is_removed = models.BooleanField(default=False)
	create_date = models.DateTimeField(auto_now_add = True,  blank = True)
	update_date = models.DateTimeField(auto_now = True, blank = True)

	#tour_packages = models.ManyToManyField(Tour_Package)
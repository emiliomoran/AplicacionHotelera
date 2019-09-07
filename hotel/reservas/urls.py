from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('busqueda-normal', views.busqueda_normal),
    # path('prueba', views.prueba)
]
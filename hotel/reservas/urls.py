from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('busqueda-normal', views.busqueda_normal),
    path('habitacion-detalles/<int:id>', views.show_details_room)
    # path('prueba', views.prueba)
]
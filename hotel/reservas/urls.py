from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('busqueda-normal', views.busqueda_normal),
    path('rooms<int:profile_id>',views.rooms, name="list_bookings"),
    # path('prueba', views.prueba)
]
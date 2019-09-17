from django.urls import path

from . import views

app_name = 'reservas'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('busqueda-normal', views.busqueda_normal),
    path('rooms<int:profile_id>',views.rooms, name="list_bookings"),
    path('habitacion-detalles/<int:id>', views.show_details_room),
    path('add-to-cart/<int:id_cuarto>',views.add_to_cart, name="add-to-cart"),
    path('prueba', views.prueba)
]
from django.urls import path

from . import views

app_name = 'administracion'

urlpatterns = [
    path('', views.index),
    path('rooms',views.RoomList.as_view(), name="room_list"),
    path('rooms/create',views.RoomCreate.as_view(), name="room_create"),
    path('rooms/editar/<int:id_room>/',views.RoomEdit.as_view(),name = 'room_edit'),
    path('rooms/eliminar/<int:id_room>/',views.RoomDelete.as_view(),name = 'room_delete'),
    path('rooms/test/',views.upload_image_room),
    path('login', views.login),
    path('logout', views.logout_admin),
    path('administradores', views.administradores),



    path('lista_reservas', views.lista_reservas),
    path('buscarcliente/', views.buscarcliente),
    path('eliminar_reserva/<int:id>', views.eliminar_reserva),
    path('agregar_reserva', views.agregar_reserva),
    path('reservas', views.reservas),
    path('nueva_reserva', views.nueva_reserva),


    path('administrador-detalle/<int:id>', views.administrador_detalle),
    path('administrador-edicion/<int:id>', views.administrador_edicion),
    path('administrador-nuevo', views.administrador_nuevo),
    path('tours',views.TourList.as_view(), name="tour_listar"),


    path('tours/crear/',views.TourCreate.as_view(),name = 'tour_crear'),
	path('tours/editar/<int:id_tour>/',views.TourEdit.as_view(),name = 'tour_editar'),
	path('tours/eliminar/<int:id_tour>/', views.TourEliminar.as_view(), name = 'tour_eliminar'), 
    ###Habitaciones disponibles###
    path('habitaciones-disponibles', views.habitaciones_disponibilidad),
    ###Habitaciones disponibles###
    path('clientes', views.clientes),
    path('makeCheckIn/<pk>/', views.makeCheckIn, name="hacer_checkin"),
]

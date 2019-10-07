from django.urls import path

from . import views

app_name = 'administracion'

urlpatterns = [
    path('', views.index),
    path('rooms',views.RoomList.as_view(), name="room_list"),
    path('rooms/create',views.RoomCreate.as_view(), name="room_create"),
    path('login', views.login),
    path('logout', views.logout_admin),
    path('administradores', views.administradores),
    path('reservas', views.reservas),
    path('administrador-detalle/<int:id>', views.administrador_detalle),
    path('administrador-edicion/<int:id>', views.administrador_edicion),
    path('administrador-nuevo', views.administrador_nuevo),    
]

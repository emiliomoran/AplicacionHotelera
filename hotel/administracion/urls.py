from django.urls import path

from . import views

app_name = 'administracion'

urlpatterns = [
    path('', views.index),
    path('rooms',views.RoomList.as_view(), name="room_list"),
    path('rooms/create',views.RoomCreate.as_view(), name="room_create"),
    path('login', views.login),
    path('administradores', views.administradores),
    path('reservas', views.reservas),
    path('detalle-administrador/<int:id>', views.detalle_administrador),
]
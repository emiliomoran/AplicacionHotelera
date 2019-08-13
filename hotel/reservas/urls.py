from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('prueba', views.prueba)
]
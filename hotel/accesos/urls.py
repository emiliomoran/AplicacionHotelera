from django.urls import include, path

from . import views

urlpatterns = [
    path('login', views.login_cliente),
    path('registro', views.registro),
    path('login_social', views.login_social),
    path('registro_social', views.registro_social),
    path('profile', views.my_profile),
]
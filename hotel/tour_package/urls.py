from django.urls import path

from . import views

app_name = 'tour_package'

urlpatterns = [
	path('', views.TourList.as_view(), name = 'tour_listar'),
	path('crear/',views.TourCreate.as_view(),name = 'tour_crear'),
	path('editar/<int:id_tour>/',views.TourEdit.as_view(),name = 'tour_editar'),
	path('eliminar/<int:id_tour>/', views.TourEliminar.as_view(), name = 'tour_eliminar'),

]
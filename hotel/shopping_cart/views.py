from django.shortcuts import render
from accesos.models import Perfil
from reservas.models import Booking
from accesos.models import Usr

# Create your views here.
def index(request):

	reservas = Booking.objects.filter(customer_id = request.session['customer']['customer_id'])
	cuartos = [reserva.room_id for reserva in reservas]

	duos = []
	for i in range(len(reservas)):
		duos.append((reservas[i],cuartos[i]))

	print(duos)
	context = {
		'reservas': duos
	}

	return render(request, 'shopping_cart/index.html', context)

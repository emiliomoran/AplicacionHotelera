from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from reservas.models import RoomType
from reservas.models import Room

# Create your views here.
def index(request):
    room_type_list = list(RoomType.objects.values('id', 'nombre'))
    # room_type_list_object = []
    # for type in room_type_list:
    #     type_object = {
    #         'id': type[0],
    #         'nombre': type[1]
    #     }
    #     room_type_list_object.append(type_object)
    print(room_type_list)

    return render(request, 'index.html', {'room_type': room_type_list})

@csrf_protect
def busqueda_normal(request):
    if request.method == 'POST':
        tipo_reserva = request.POST.get("select_tipo_reserva")
        fecha_reserva = request.POST.get("fecha_reserva")
        tipo_habitacion = request.POST.get("select_tipo_habitacion")
        num_adultos = request.POST.get("select_num_adultos")
        num_ninos = request.POST.get("select_num_ninos")

        print(tipo_reserva)
        print(fecha_reserva)        
        print(tipo_habitacion)
        print(num_adultos)
        print(num_ninos)

        #Búsqueda de habitaciones solo disponibles
        room_list_filter_1 = list(Room.objects.values('id', 'precio', 'calificacion', 'path_image', 'id_roomtype_id__nombre').filter(disponible=True, id_roomtype_id=int(tipo_habitacion), num_adultos=int(num_adultos), num_ninos=int(num_ninos)))        
        print(room_list_filter_1)

        return render(request, 'rooms_filter.html', {'rooms_1': room_list_filter_1})

# def prueba(request):
#     print('###################')
#     print(request.user.id)    
#     print(request.user.extra_data)    
#     print('###################')
#     return render(request, 'prueba.html')

def rooms(request,profile_id):
    objects_list = Booking.objects.filter(customer_id=profile_id)
    context =  {
        'reservas': objects_list
    }

    return render(request,"list_reservas.html",context)
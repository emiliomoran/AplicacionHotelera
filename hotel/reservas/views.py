from django.shortcuts import render
from django.db.models import Q
from datetime import datetime
from django.views.decorators.csrf import csrf_protect
from reservas.models import RoomType
from reservas.models import Room
from reservas.models import Booking
from reservas.models import BookingType
from reservas.models import BookingState
from accesos.models import Usr, Perfil
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from reservas.forms import RoomForm
from django.shortcuts import redirect
from django.http import HttpResponse 


def index(request):
    room_type_list = list(RoomType.objects.values('id', 'nombre'))
    booking_type_list = list(BookingType.objects.values('id', 'name'))
    print(room_type_list)
    print(booking_type_list)
    return render(request, 'index.html', {'room_type': room_type_list, 'booking_type': booking_type_list})


@csrf_protect
def busqueda_normal(request):
    if request.method == 'POST':
        tipo_reserva = request.POST.get("select_tipo_reserva")
        fecha_reserva = request.POST.get("fecha_reserva")
        print(tipo_reserva)
        print(fecha_reserva)
        if(tipo_reserva == '1'):
            tipo_habitacion = request.POST.get("select_tipo_habitacion")
            num_adultos = request.POST.get("select_num_adultos")
            num_ninos = request.POST.get("select_num_ninos")
            print(tipo_habitacion)
            print(num_adultos)
            print(num_ninos)

            # Búsqueda de habitaciones solo disponibles
            room_list_filter_1 = list(Room.objects.values('id', 'precio', 'calificacion', 'path_image', 'id_roomtype_id__nombre').filter(
                disponible=True, id_roomtype_id=int(tipo_habitacion), num_adultos=int(num_adultos), num_ninos=int(num_ninos)))
            print(room_list_filter_1)

            # Búsqueda de habitaciones reservadas pero que cumplen con el rango de fechas
            check_in_date = convert_date(fecha_reserva.split(' - ')[0])
            check_out_date = convert_date(fecha_reserva.split(' - ')[1])

            print(check_in_date)
            print(check_out_date)

            out_queries = Room.objects.raw('''
                select r.id as id, r.precio as precio, r.calificacion as calificacion, r.path_image as path_image, rt.nombre as id_roomtype_id__nombre
                from reservas_room as r, reservas_roomtype as rt
                where r.id_roomtype_id=rt.id
                and disponible = %s
                and num_adultos = %s
                and num_ninos = %s
                and id_roomtype_id=%s
                and r.id not in
                (
                    select distinct b.room_id_id
                    from reservas_booking as b, reservas_bookingstate as bs, reservas_bookingtype as bt
                    where b.state_id_id = bs.id
                    and b.bookingtype_id_id = bt.id
                    and b.check_out_date > %s
                    and b.check_in_date < %s
                    and bs.name != %s
                    and bt.name = %s                
                )
            ''', [False, int(num_adultos), int(num_ninos), int(tipo_habitacion), check_in_date, check_out_date, 'Pasada', 'Normal'])

            for e in out_queries:
                room_list_filter_1.append(e)

            print(room_list_filter_1)

            return render(request, 'rooms_filter.html', {'rooms_1': room_list_filter_1})
        else:
            num_invitados = request.POST.get("select_num_invitados")
            print(num_invitados)
            return render(request, 'rooms_filter.html')


def show_details_room(request, id):
    room_details = list(Room.objects.values('id', 'descripcion', 'path_image', 'calificacion',
                                            'num_camas', 'num_adultos', 'num_ninos', 'precio', 'id_roomtype_id__nombre').filter(id=id))
    print(room_details)

    return render(request, 'rooms_single.html', {'room_details': room_details[0]})


def convert_date(string_date):
    dia = string_date.split('/')[0]
    mes = string_date.split('/')[1]
    ano = string_date.split('/')[2]

    return ano+'-'+mes+'-'+dia


def rooms(request, profile_id):
    objects_list = Booking.objects.filter(customer_id=profile_id)
    context = {
        'reservas': objects_list
    }

    return render(request, "list_reservas.html", context)

# @login_required(login_url = '/accesos/login')#revisar para mantener el login.
def add_to_cart(request, id_cuarto):

    if request.method == "POST":
        try:
            print('###################################')
            print(request.session['customer'])
            print('###################################')
            perfil = get_object_or_404(
                Perfil, id=request.session["customer"]['customer_id'])
            #cliente = Cliente.objects.filter(id=1).first()
            #perfil = Perfil.objects.filter(usuario=cliente).first()
            # Lo siguiente deberia ser considerado como un Producto de manera general, pero por ahora sera un cuarto.
            cuarto = Room.objects.filter(id=id_cuarto).first()
            booking_type = BookingType.objects.filter(id=1).first()
            booking_state = BookingState.objects.filter(id=1).first()

            print(perfil)
            booking = Booking(
                customer_id=perfil,
                room_id=cuarto,
                bookingtype_id=booking_type,
                state_id=booking_state,
                booking_date=datetime.now(),
                no_nights=3
            )
            booking.save()

            return redirect('reservas:index')

        except Exception as error:
            print(error)
            # return render(request,"index.html")

    else:
        print("Ya fue")

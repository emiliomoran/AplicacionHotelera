from django.shortcuts import redirect, render
from reservas.models import Room, BookingState, BookingType
from accesos.models import Usr, Perfil
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView,DeleteView
from administracion.forms import RoomForm, TourForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout

from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response

from datetime import date
from datetime import datetime
import dateutil.parser

from django.core.files.storage import FileSystemStorage
from django.db.models import Max

import datetime

from django.http import JsonResponse

# Modelos
from accesos.models import Usr
from accesos.models import Perfil
from reservas.models import Booking

from tour_package.models import Tour_Package

def index(request):
    if('success_login' in request.session and request.session['success_login']):
        return render(request, 'index-admin.html')
    return redirect('/administracion/login')

def reservas(request):
    template_name = 'reservas/reservas-admin.html'
    return render(request, template_name)


class RoomList(ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'rooms/index_rooms.html'


class RoomCreate(CreateView):
    model = Room
    form_class = RoomForm
    template_name = "rooms/create_room.html"

    success_url = reverse_lazy("administracion:room_list")

def upload_image_room(request):

    if request.method == 'POST':
        file = request.FILES['path_image']
        form = RoomForm(request.POST,request.FILES)
        fs = FileSystemStorage()

        if form.is_valid():
            numero_cuarto = get_last_item_id() + 1
            nombre_imagen = "imagen_cuarto_"+ str(numero_cuarto) + '.' + (file.name.split('.'))[1]
            fs.save(nombre_imagen,file)
            form.save()
            return redirect('/administracion/')
    else:
        form = RoomForm()
    
    return render(request,'rooms/index_rooms.html',{'form':form})

def get_last_item_id():
    if len(Room.objects.all()) > 0:
        return Room.objects.all().order_by("-id")[0].id
    else:
        return 0
class RoomEdit(UpdateView):

    model = Room
    context_object_name = 'room'
    template_name = 'rooms/room_edit.html'
    form_class = RoomForm

    def get_object(self):
        id_ = self.kwargs.get("id_room")
        return get_object_or_404(Room,id = id_)

    success_url = reverse_lazy("administracion:room_list")

class RoomDelete(DeleteView):
    model = Room
    success_url = reverse_lazy("administracion:room_list")
    template_name = 'rooms/room_delete_form.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id_room")
        return get_object_or_404(Room,id = id_)

###Accesos de administrador###

def login(request):
    if request.method == 'POST':
        print("Post")
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email is None or password is None:
            # return HttpResponse("Por favor ingrese el email y contrasena!")
            request.session['success_login'] = False
            return redirect('/administracion/login')
        try:
            usr = Usr.objects.get(email=email, is_admin=True)
            # print(password)
            # print(usr.password)
            if(check_password(password, usr.password)):
                perfil = Perfil.objects.get(usr_id_id=usr.id)
                request.session['success_login'] = True
                request.session.modified = True
                # print(perfil.name)    Para verificar si toma el perfil
                customer_json = {
                    'customer_id': perfil.id,
                    'name': perfil.name,
                    'last_name': perfil.last_name,
                    'date_birth': str(perfil.date_birth),
                    'email': usr.email,
                    'username': usr.username
                }

                print(customer_json)
                request.session['customer'] = customer_json

                return redirect('/administracion')
            else:
                print("entra a false")
                request.session['success_login'] = False
                return redirect('/administracion/login')

        except Exception as error:
            print(error)
            request.session['success_login'] = False
            return redirect('/administracion/login')
    else:        
        if('success_login' in request.session and request.session['success_login']):
            return redirect('/administracion')
        return render(request, 'accesos/login.html')

def logout_admin(request):
    logout(request)
    return redirect('/administracion/login')

###Accesos de administrador###

###Administracion de administradores###

def administradores(request):
    admin_list = []
    out_queries = Perfil.objects.raw('''
        select ap.id, ap.name, ap.last_name, au.email, au.is_removed
        from accesos_perfil as ap, accesos_usr as au
        where ap.usr_id_id = au.id
        and au.is_admin = true;
    ''')

    for e in out_queries:
        admin_list.append(e)

    print(admin_list)
    return render(request, 'admin_administradores/administradores.html', {'administradores': admin_list})

def administrador_detalle(request, id):
    admin_details = list(Perfil.objects.values('id', 'name', 'last_name',
                                               'phone', 'date_birth', 'usr_id_id__email', 'is_removed').filter(id=id))
    print(admin_details)

    return render(request, 'admin_administradores/administrador_detalle.html', {'administrador': admin_details[0]})


def administrador_edicion(request, id):
    if request.method == 'POST':
        name = request.POST.get('nombres')
        last_name = request.POST.get('apellidos')
        date_birth = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        phone = request.POST.get('telf')
        is_removed = request.POST.get('is_removed')

        perfil = Perfil.objects.get(id=id)
        usr = Usr.objects.get(id=perfil.usr_id_id)

        perfil.name = name
        perfil.last_name = last_name
        perfil.date_birth = date_birth
        perfil.phone = phone
        if(is_removed == '0'):
            perfil.is_removed = True
        else:
            perfil.is_removed = False
        usr.email = email
        if(is_removed == '0'):
            usr.is_removed = True
        else:
            usr.is_removed = False

        perfil.save()
        usr.save()

        return redirect('/administracion/administradores')

    else:
        admin = list(Perfil.objects.values('id', 'name', 'last_name', 'phone',
                                           'date_birth', 'usr_id_id__email', 'is_removed').filter(id=id))
        admin[0]['date_birth'] = admin[0]['date_birth'].strftime("%Y-%m-%d")
        print(admin)

        return render(request, 'admin_administradores/administrador_edicion.html', {'administrador': admin[0]})


def administrador_nuevo(request):
    if request.method == "POST":
        name = request.POST.get('nombres')
        last_name = request.POST.get('apellidos')
        date_birth = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        phone = request.POST.get('telf')
        password_hash = make_password('Admin2019')
        
        usr = Usr(
            username=email.split('@')[0],
            email=email,
            password=password_hash,
            is_admin=True
        )

        usr.save()

        perfil = Perfil(
            usr_id=usr,
            name=name,
            last_name=last_name,
            date_birth=date_birth,
            phone=phone,
        )

        perfil.save()

        return redirect('/administracion/administradores')

    else:
        return render(request, 'admin_administradores/administrador_nuevo.html')





###Administracion de administradores###

###Habitaciones disponibles###



###Habitaciones disponibles###
def habitaciones_disponibilidad(request):
    room_list = []
    room_list = list(Room.objects.values('id', 'descripcion', 'calificacion', 'num_camas', 'num_adultos', 'num_ninos', 'precio', 'disponible', 'id_roomtype_id__nombre'))
    print(room_list)
    return render(request, 'habitaciones_disponibles/habitaciones_disponibles.html', {'habitaciones_disponibles': room_list})



###Administracion de reservas###

def lista_reservas(request):
    reservas_list = []
    out_queries = Booking.objects.raw('''
        select b.id, b.check_in_date, b.check_out_date, p.name, p.last_name, r.descripcion
        from reservas_booking as b, accesos_perfil as p, reservas_room as r
        where b.customer_id_id = p.id and b.room_id_id = r.id and b.state_id_id > 1
    ''')
    for e in out_queries:
        reservas_list.append(e)
        print(type(e.check_in_date))

    return render(request, 'reservas/reservas-admin.html', {'lista_reservas': reservas_list})

def eliminar_reserva(request, id):
    Booking.objects.filter(id=id).delete()
    return render(request, 'reservas/reservas-admin.html', {'lista_reservas': reservas_list})

def agregar_reserva(request):
    return render(request, 'reservas/addreserva.html')

def buscarcliente(request):
    ced = request.GET.get('cedula', None)
    print("cedula"+ced)
    is_taken = Perfil.objects.filter(cedula__iexact=ced).exists()
    user = Perfil.objects.filter(cedula=ced)[0]
    u = Usr.objects.filter(id=user.usr_id_id)[0]
    print(u)
    if(is_taken):
        data = {
           'existe': is_taken,
           'nombres': user.name,
           'apellidos': user.last_name,
           'fecha_nacimiento': user.date_birth,
           'telfono': user.phone,
           'email': u.email
        }
    else:
        data = {
         'existe': is_taken
        }
    return JsonResponse(data)
   
    
def nueva_reserva(request):
    if request.method == "POST":
        ced = request.POST.get('cedula')
        name = request.POST.get('nombres')
        last_name = request.POST.get('apellidos')
        date_birth = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        phone = request.POST.get('telf')
        ingreso = request.POST.get('fechain')
        salida = request.POST.get('fechasal')
        password_hash = make_password(ced)
        room = Room.objects.get(id = 1)
        estado = request.POST.get('estado')
        #cliente
        is_taken = Perfil.objects.filter(cedula__iexact=ced).exists()
        print(is_taken)
        if(is_taken):
            perfil = Perfil.objects.filter(cedula=ced)[0]
        else:
            usr = Usr(
                username=email.split('@')[0],
                email=email,
                password=password_hash,
                is_admin=False
            )

            usr.save()

            perfil = Perfil(
                usr_id=usr,
                cedula = ced,
                name=name,
                last_name=last_name,
                date_birth=date_birth,
                phone=phone,
            )

            perfil.save()
        r_estado = BookingState.objects.get(id=estado)
        r_tipo = BookingType.objects.get(id = 1)
            

        reserva = Booking(
            check_in_date = ingreso,
            check_out_date = salida,
            room_id = room,
            customer_id = perfil,
            state_id = r_estado,
            bookingtype_id = r_tipo

        )
        reserva.save()

        return redirect('/administracion/lista_reservas')

    else:
        return render(request, 'reservas/administrador_nuevo.html')

def buscarhabitaciones(request):
    fechain= request.GET.get('fechain', None)
    fechaout= request.GET.get('fechaout', None)
    num = request.GET.get("tipo", None)
    
    adultos = request.GET.get("select_num_adultos", None)
    ninos = request.GET.get("select_num_ninos", None)
    rooms_list = []
    
    # Búsqueda de habitaciones solo disponibles
    room_list_filter_1 = list(Room.objects.values('id', 'precio', 'calificacion', 'id_roomtype_id__nombre').filter(
                disponible=True, id_roomtype_id=num, num_adultos=adultos, num_ninos=ninos))
    check_in_date = fechain
    check_out_date =fechaout
    out_queries = Room.objects.raw('''
                select r.id as id, r.precio as precio, r.calificacion as calificacion, rt.nombre as id_roomtype_id__nombre
                from reservas_room as r, reservas_roomtype as rt
                where r.id_roomtype_id=rt.id
                and disponible = %s
                and num_adultos = %s
                and num_ninos = %s
                and id_roomtype_id = %s
                and r.id not in
                (
                    select distinct b.room_id_id
                    from reservas_booking as b, reservas_bookingstate as bs, reservas_bookingtype as bt
                    where b.state_id_id = bs.id
                    and b.bookingtype_id_id = bt.id
                    and b.check_out_date > %s
                    and b.check_in_date < %s)
            ''',[True, adultos, ninos, num, check_out_date, check_in_date])
    for e in out_queries:
        room_list_filter_1.append(e)
    
    print(room_list_filter_1)
    return render(request, 'reservas/addreserva.html', {'habitaciones_disponibles': room_list_filter_1})
   
def convert_date(string_date):
    dia = string_date.split('-')[2]
    mes = string_date.split('-')[1]
    ano = string_date.split('-')[0]

    return ano+'-'+mes+'-'+dia

###Administracion de reservas###


###Administracion de clientes###

def clientes(request):
    clientes_list = []
    out_queries = Perfil.objects.raw('''
        select ap.id, ap.name, ap.last_name, au.email, ap.phone, ap.date_birth, au.is_removed
        from accesos_perfil as ap, accesos_usr as au
        where ap.usr_id_id = au.id
        and au.is_admin = false
        and au.is_staff = false
        and au.is_superuser=false;
    ''')

    for e in out_queries:
        clientes_list.append(e)

    print(clientes_list)
    return render(request, 'clientes/clientes.html', {'clientes': clientes_list})

###Administracion de clientes###

class makeCheckInView(views.APIView):
    def post(self, request, pk):
        bookingActual = get_object_or_404(Booking, pk = pk) #Booking.bookings.get_object(pk = pk)
        print(Booking.objects)
        print("TEST")
        fecha_ingreso = datetime.datetime.now()
        bookingActual.fecha_ingresado = fecha_ingreso
        bookingActual.save()
        respuesta = { 'detail' :  fecha_ingreso}
        return JsonResponse(respuesta)


####PAQUETES TURISTICOS####
class TourList(ListView):
    
    model = Tour_Package
    context_object_name = 'tours'
    template_name = 'tour-package/index_tours.html'

class TourCreate(CreateView):

    model = Tour_Package
    form_class = TourForm
    template_name = "tour-package/tour_create_form.html"

    success_url = reverse_lazy("administracion:tour_listar")

class TourEdit(UpdateView):

    model = Tour_Package
    context_object_name = 'tour'
    template_name = 'tour-package/tour_edit.html'
    form_class = TourForm

    def get_object(self):
        id_ = self.kwargs.get("id_tour")
        return get_object_or_404(Tour_Package,id = id_)

    success_url = reverse_lazy("administracion:tour_listar")

class TourEliminar(DeleteView):
    model = Tour_Package
    success_url = reverse_lazy("administracion:tour_listar")
    template_name = 'tour-package/tour_delete_form.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id_tour")
        return get_object_or_404(Tour_Package,id = id_)
        
        
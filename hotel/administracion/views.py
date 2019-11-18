from django.shortcuts import redirect, render
from reservas.models import Room, BookingState, BookingType, RoomType
from accesos.models import Usr, Perfil
from administracion.choices import TIPO_DE_IDENTIFICACION, GENERO
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from administracion.forms import RoomForm, TourForm, DocumentForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout

from rest_framework import generics
from rest_framework import views
from rest_framework.response import Response

# from datetime import date
# from datetime import datetime
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


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/administracion/')
    else:
        form = DocumentForm()
    return render(request, 'rooms/documento_form.html', {
        'form': form
    })


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


def room_create_form(request):
    if request.method == 'POST':
        form = RoomForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/administracion/')
    else:
        form = RoomForm()
    return render(request, 'rooms/create_room.html', {
        'form': form
    })


class RoomCreate(CreateView):
    model = Room
    form_class = RoomForm
    template_name = "rooms/create_room.html"

    success_url = reverse_lazy("administracion:room_list")


def upload_image_room(request):

    if request.method == 'POST':
        file = request.FILES['path_image']
        form = RoomForm(request.POST, request.FILES)
        fs = FileSystemStorage()

        if form.is_valid():
            numero_cuarto = get_last_item_id() + 1
            nombre_imagen = "imagen_cuarto_" + \
                str(numero_cuarto) + '.' + (file.name.split('.'))[1]
            fs.save(nombre_imagen, file)
            form.save()
            return redirect('/administracion/')
    else:
        form = RoomForm()

    return render(request, 'rooms/index_rooms.html', {'form': form})


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
        return get_object_or_404(Room, id=id_)

    success_url = reverse_lazy("administracion:room_list")


class RoomDelete(DeleteView):
    model = Room
    success_url = reverse_lazy("administracion:room_list")
    template_name = 'rooms/room_delete_form.html'

    def get_object(self):
        id_ = self.kwargs.get("id_room")
        return get_object_or_404(Room, id=id_)

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
        and au.is_admin = true
        and ap.is_removed = false
        and au.is_removed = false;
    ''')

    for e in out_queries:
        print(e)
        admin_list.append(e)

    print(admin_list)
    return render(request, 'admin_administradores/administradores.html', {'administradores': admin_list,
                                                                          'choices': TIPO_DE_IDENTIFICACION, 'genero': GENERO})


def administrador_eliminacion(request, id):
    perfil = Perfil.objects.get(id=id)
    usr = Usr.objects.get(id=perfil.usr_id_id)

    perfil.is_removed = True
    perfil.update_date = datetime.datetime.now()
    usr.is_removed = True
    usr.update_date = datetime.datetime.now()

    perfil.save()
    usr.save()

    return redirect('/administracion/administradores')


def administrador_edicion(request, id):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('nombres')
        last_name = request.POST.get('apellidos')
        date_birth = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        phone = request.POST.get('telf')
        is_removed = request.POST.get('is_removed')
        cedula = request.POST.get('documento')
        doc_type = request.POST.get('dropwdown-docs')
        genero = request.POST.get('dropwdown-generos')

        perfil = Perfil.objects.get(id=id)
        usr = Usr.objects.get(id=perfil.usr_id_id)

        perfil.name = name
        perfil.last_name = last_name
        perfil.date_birth = date_birth
        perfil.phone = phone
        cedula = cedula,
        doc_type = doc_type,
        genero = genero

        perfil.save()
        usr.save()

        return redirect('/administracion/administradores')

    else:
        admin = list(Perfil.objects.values('id', 'name', 'last_name', 'phone',
                                           'date_birth', 'usr_id_id__email', 'is_removed', 'cedula', 'doc_type', 'genero').filter(id=id))
        admin[0]['date_birth'] = admin[0]['date_birth'].strftime("%Y-%m-%d")
        print(admin)

        return render(request, 'admin_administradores/administrador_edicion.html', {
            'administrador': admin[0],
            'docs': TIPO_DE_IDENTIFICACION,
            'generos': GENERO
        })


def administrador_nuevo(request):
    if request.method == "POST":
        print(request.POST)
        name = request.POST.get('nombres')
        last_name = request.POST.get('apellidos')
        date_birth = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        phone = request.POST.get('telf')
        password_hash = make_password('Admin2019')
        cedula = request.POST.get('documento')
        doc_type = request.POST.get('dropwdown-docs')
        genero = request.POST.get('dropwdown-generos')

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
            cedula=cedula,
            doc_type=doc_type,
            genero=genero
        )

        perfil.save()

        return redirect('/administracion/administradores')

    else:
        return render(request, 'admin_administradores/administrador_nuevo.html', {
            'docs': TIPO_DE_IDENTIFICACION,
            'generos': GENERO})


###Administracion de administradores###

###Habitaciones disponibles###


###Habitaciones disponibles###
def habitaciones_disponibilidad(request):
    room_list = []
    room_list = list(Room.objects.values('id', 'descripcion', 'calificacion', 'num_camas',
                                         'num_adultos', 'num_ninos', 'precio', 'disponible', 'id_roomtype_id__nombre'))
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
    if request.method == 'POST':
        print(request.GET)
        
    room_type_list = list(RoomType.objects.values('id', 'nombre'))
    return render(request, 'reservas/addreserva.html', {'choices_id': TIPO_DE_IDENTIFICACION, 'room_type': room_type_list})


def buscarcliente(request):
    ced = request.GET.get('cedula', None)
    doc_type = request.GET.get('tipo_documento', None)
    """ print("cedula"+ced) """
    is_taken = Perfil.objects.filter(
        cedula__iexact=ced, doc_type=doc_type).exists()
    if(is_taken):
        user = Perfil.objects.filter(cedula=ced)[0]
        u = Usr.objects.filter(id=user.usr_id_id)[0]
        data = {
            'existe': is_taken,
            'nombres': user.name,
            'apellidos': user.last_name,
            'fecha_nacimiento': user.date_birth.strftime("%Y-%m-%d"),
            'telfono': user.phone,
            'email': u.email
        }
        print(data)
    else:
        data = {
            'existe': False
        }
    return JsonResponse(data)

def buscarhabitaciones(request):
    print(request.GET)
    """ fechain = request.GET.get('fechain')
    fechaout = request.GET.get('fechaout')
    num = request.GET.get("tipo")
    adultos = request.GET.get("select_num_adultos")
    ninos = request.GET.get("select_num_ninos")
    room_list = []

    # Búsqueda de habitaciones solo disponibles

    out_queries = Room.objects.raw('''
               select r.id as id, r.precio as precio, rt.nombre as id_roomtype_id__nombre
                from reservas_room as r, reservas_roomtype as rt
                where r.id_roomtype_id=rt.id
                and disponible = true
                and num_adultos = 2
                and num_ninos = 1
                and id_roomtype_id = 1
                and r.id not in 
				(
                    select distinct b.room_id_id
                    from reservas_booking as b, reservas_bookingstate as bs, reservas_bookingtype as bt
                    where b.state_id_id = bs.id
                    and b.bookingtype_id_id = bt.id
                    and b.check_out_date > '2020-11-10'
                    and b.check_in_date < '2020-11-10') ''')
    for e in out_queries:
        room_list.append(e)
        print(e)

    print(room_list)
    return render(request, 'reservas/addreserva.html', {'habitaciones_disponibles': room_list}) """


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
        select ap.id, ap.name, ap.last_name, ap.cedula, ap.genero, au.email, ap.phone, ap.date_birth, au.is_removed
        from accesos_perfil as ap, accesos_usr as au
        where ap.usr_id_id = au.id
        and au.is_admin = false
        and au.is_staff = false
        and au.is_superuser=false;
    ''')

    for e in out_queries:
        if(e.cedula == None):
            e.phone = 'Sin dato'
        if(e.phone == None):
            e.phone = 'Sin dato'
        clientes_list.append(e)

    print(clientes_list)
    return render(request, 'clientes/clientes.html', {'clientes': clientes_list})

###Administracion de clientes###


class makeCheckInView(views.APIView):
    def post(self, request, pk):
        # Booking.bookings.get_object(pk = pk)
        bookingActual = get_object_or_404(Booking, pk=pk)
        print(Booking.objects)
        print("TEST")
        fecha_ingreso = datetime.datetime.now()
        bookingActual.fecha_ingresado = fecha_ingreso
        bookingActual.save()
        respuesta = {'detail':  fecha_ingreso}
        return JsonResponse(respuesta)


class makeCheckOutView(views.APIView):
    def post(self, request, pk):
        # Booking.bookings.get_object(pk = pk)
        bookingActual = get_object_or_404(Booking, pk=pk)
        print(Booking.objects)
        print("TEST")
        fecha_salida = datetime.datetime.now()
        bookingActual.fecha_salida = fecha_salida
        bookingActual.save()
        respuesta = {'detail':  fecha_salida}
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
        return get_object_or_404(Tour_Package, id=id_)

    success_url = reverse_lazy("administracion:tour_listar")


class TourEliminar(DeleteView):
    model = Tour_Package
    success_url = reverse_lazy("administracion:tour_listar")
    template_name = 'tour-package/tour_delete_form.html'

    def get_object(self):
        id_ = self.kwargs.get("id_tour")
        return get_object_or_404(Tour_Package, id=id_)

from django.shortcuts import redirect, render
from reservas.models import Room
from accesos.models import Usr, Perfil
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView,DeleteView
from administracion.forms import RoomForm, TourForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import logout
from django.core.files.storage import FileSystemStorage
from django.db.models import Max
import datetime

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
    template_name = 'reservas-admin.html'
    return render(request, template_name)


class RoomList(ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'rooms/index_rooms.html'


class RoomCreate(CreateView):
    model = Room
    form_class = RoomForm
    template_name = "rooms/create_room.html"

    success_url = reverse_lazy("reservas:room_list")

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
        select b.id, b.check_in_date, b.check_out_date, p.name, p.last_name
        from reservas_booking as b, accesos_perfil as p
        where b.customer_id_id = p.id
       
    ''')

    for e in out_queries:
        reservas_list.append(e)
        print(e)

    
    return render(request, 'reservas-admin.html', {'lista_reservas': reservas_list})

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

def makeCheckIn(request, pk):
    bookingActual = Booking.objects.get_object_or_404(pk = pk)
    bookingActual.check_in_date = datetime.datetime.now()
    bookingActual.save()

    return render(request, 'clientes/clientes.html')

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
        
        
from django.shortcuts import redirect, render
from reservas.models import Room
from django.views.generic import ListView,CreateView
from administracion.forms import RoomForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

# Modelos
from accesos.models import Usr
from accesos.models import Perfil

def index(request):
    print("Entra a index")
    template_name = 'index-admin.html'
    return render(request, template_name)

class RoomList(ListView):
    model = Room
    context_object_name = 'rooms'
    template_name = 'index_rooms.html'

class RoomCreate(CreateView):
    model = Room
    form_class = RoomForm
    template_name = "create_room.html"

    success_url = reverse_lazy("reservas:room_list")

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
        return render(request, 'login.html')

def administradores(request):
    return render(request, 'administradores.html')
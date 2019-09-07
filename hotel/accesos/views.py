from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import make_password, check_password

# Modelos
from accesos.models import Cliente
from accesos.models import Perfil

# Create your views here.


@csrf_protect
def login_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email is None or password is None:
            return HttpResponse("Por favor ingrese el email y contrasena!")
        try:
            cliente = Cliente.objects.get(email=email)
            # print(cliente.nombres)
            print(password)
            print(cliente.password)
            if(check_password(password, cliente.password)):
                print("entra a true")                
                request.session['estado'] = True
                json_cliente = {
                    'nombres': cliente.nombres,
                    'apellidos': cliente.apellidos,
                    'fecha_nacimiento': str(cliente.fecha_nacimiento),
                    'email': cliente.email
                }
    
                request.session['cliente'] = json_cliente
    
                return redirect('/reservas')
            else:
                print("entra a false")
                return HttpResponse("No existe!")            
            
        except Exception as error:
            print(error)
            return HttpResponse("No existe!")
    else:
        return render(request, 'login_cliente.html')

@csrf_protect
def registro(request):
    if request.method == 'POST':
        try:
            nombres = request.POST.get('nombres')
            apellidos = request.POST.get('apellidos')
            fecha_nacimiento = request.POST.get('fecha_nacimiento')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password_hash = make_password(password)
            print(password)
            print(password_hash)

            cliente = Cliente(
                nombres=nombres,
                apellidos=apellidos,
                fecha_nacimiento=fecha_nacimiento,
                email=email,
                password=password_hash
            )

            cliente.save()

            Perfil.objects.create(
                usuario = cliente
            )


            return redirect('/accesos/login')

        except Exception as error:
            print(error)

    else:
        return render(request, 'registro_form.html')


def login_social(request):
    try:
        cliente = Cliente.objects.get(id=request.user.id)
        request.session['estado'] = True
        json_cliente = {
            'nombres': cliente.nombres,
            'apellidos': cliente.apellidos,
            'fecha_nacimiento': str(cliente.fecha_nacimiento),
            'email': cliente.email
        }

        request.session['cliente'] = json_cliente

        return redirect('/reservas')
    except Exception as error:
        print(error)

@csrf_protect
def registro_social(request):
    if request.method == 'POST':
        try:
            cliente = Cliente.objects.get(id=request.user.id)
            cliente.nombres = request.POST.get('nombres')
            cliente.apellidos = request.POST.get('apellidos')
            cliente.fecha_nacimiento = request.POST.get('fecha_nacimiento')
            cliente.save()

            cliente_actualizado = Cliente.objects.get(id=request.user.id)
            json_cliente = {
                'nombres': cliente_actualizado.nombres,
                'apellidos': cliente_actualizado.apellidos,
                'fecha_nacimiento': str(cliente_actualizado.fecha_nacimiento),
                'email': cliente_actualizado.email
            }

            request.session['cliente'] = json_cliente
            return redirect('/reservas')

        except Exception as error:
            print(error)
    else:
        try:
            cliente = Cliente.objects.get(id=request.user.id)
            request.session['estado'] = True
            json_cliente = {
                'nombres': cliente.nombres,
                'apellidos': cliente.apellidos,
                'fecha_nacimiento': cliente.fecha_nacimiento,
                'email': cliente.email
            }
            request.session['cliente'] = json_cliente

            return render(request, 'registro_social.html')
        except Exception as error:
            print(error)

def my_profile(request):
	my_user_profile = Perfil.objects.filter(usuario = request.usuario).first()
	my_reservations = Reservas.objects.filter(estaReservado = True, owner = my_user_profile)
	
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.hashers import make_password, check_password

# Modelos
from accesos.models import Usr
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
            usr = Usr.objects.get(email=email)
            # print(password)
            # print(usr.password)
            if(check_password(password, usr.password)):
                perfil = Perfil.objects.get(usr_id_id=usr.id)
                if 'success_register' in request.session:
                    del request.session['success_register']
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

                return redirect('/reservas')
            else:
                print("entra a false")
                request.session['success_login'] = False
                return redirect('/accesos/login')

        except Exception as error:
            print(error)
            request.session['success_login'] = False
            return redirect('/accesos/login')
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

            usr = Usr(
                username=email.split('@')[0],
                email=email,
                password=password_hash,
                is_admin=False
            )

            usr.save()

            perfil = Perfil(
                usr_id=usr,
                name=nombres,
                last_name=apellidos,
                date_birth=fecha_nacimiento,
            )

            perfil.save()

            request.session['success_register'] = True
            return redirect('/accesos/login')

        except Exception as error:
            print(error)
            request.session['success_register'] = False
            return redirect('/accesos/login')
    else:
        return render(request, 'registro_form.html')


def login_social(request):
    try:
        usr = Usr.objects.get(id=request.user.id)

        perfil = Perfil.objects.get(usr_id_id=usr.id)

        if 'success_register' in request.session:
            del request.session['success_register']
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

        return redirect('/reservas')

    except Exception as error:
        print(error)
        request.session['success_register'] = False
        return redirect('/accesos/login')


@csrf_protect
def registro_social(request):
    if request.method == 'POST':
        try:
            usr = Usr.objects.get(id=request.user.id)

            perfil = Perfil(
                usr_id=usr,
                name=request.POST.get('nombres'),
                last_name=request.POST.get('apellidos'),
                date_birth=request.POST.get('fecha_nacimiento'),
            )

            perfil.save()

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

            return redirect('/reservas')
        except Exception as error:
            print(error)
            request.session['success_register'] = False
            return redirect('/accesos/login')
    else:
        try:
            usr = Usr.objects.get(id=request.user.id)

            if 'success_register' in request.session:
                del request.session['success_register']
            request.session['success_login'] = True
            request.session.modified = True

            customer_json = {
                'email': usr.email,
                'username': usr.username
            }

            print(customer_json)
            request.session['customer'] = customer_json

            return render(request, 'registro_social.html')

        except Exception as error:
            print(error)
            request.session['success_register'] = False
            return redirect('/accesos/login')


def my_profile(request):
    my_user_profile = Perfil.objects.filter(usuario=request.usuario).first()
    my_reservations = Reservas.objects.filter(
        estaReservado=True, owner=my_user_profile)

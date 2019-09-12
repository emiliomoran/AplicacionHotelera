from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from accesos.models import Usr, Perfil
from django.contrib.auth.hashers import make_password, check_password


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')
        if email is None or password is None:
            return Response(
                {
                    'error': True,
                    'message_error': 'Por favor, ingresar email y contraseña!'
                }, status=HTTP_400_BAD_REQUEST)

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
            # token, _  = Token.objects.get_or_create(user=usr)
            customer_json = {
                'customer_id': perfil.id,
                'name': perfil.name,
                'last_name': perfil.last_name,
                'date_birth': str(perfil.date_birth),
                'email': usr.email,
                'username': usr.username,
                # 'token': token.key
            }

            print(customer_json)
            request.session['customer'] = customer_json

            return Response(
                {
                    'error': False,
                    'customer': customer_json
                }, status=HTTP_200_OK)
        else:
            print("entra a false")
            request.session['success_login'] = False
            return Response(
                {
                    'error': True,
                    'message_error': 'Credenciales inválidas!'
                }, status=HTTP_404_NOT_FOUND)
    except Exception as error:
        print(error)
        print("entra a false")
        request.session['success_login'] = False
        return Response(
            {
                'error': True,
                'message_error': 'Error en la aplicación!'
            }, status=HTTP_404_NOT_FOUND)

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def registro(request):
    try:
        print("ENTRAAAAAA API REGISTER")
        nombres = request.POST.get('nombres')
        apellidos = request.POST.get('apellidos')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_hash = make_password(password)

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

        return Response(
            {
                'error': False,
                'message_success': 'Se ha registrado exitosamente!'
            }, status=HTTP_200_OK)

    except Exception as error:
        print(error)
        print("entrar a error")
        return Response(
            {
                'error': True,
                'message_error': 'Falló el registro!'
            }, status=HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)

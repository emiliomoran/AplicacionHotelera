from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

#Modelos
from accesos.models import Cliente

# Create your views here.

@csrf_protect
def login_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email is None or password is None:
            return HttpResponse("Por favor ingrese el email y contrasena!")
        try:
            cliente = Cliente.objects.get(email = email, password = password)
            # print(cliente.nombres)
            request.session['estado'] = True
            request.session['nombres'] = cliente.nombres
            return redirect('/reservas')
        except Exception as error:
            print(error)
            return HttpResponse("No existe!")
    else:
        return render(request, 'login_cliente.html')



from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def index(request):
    # print(request.session['nombres'])
    print('###################')    
    print(request.user.id)    
    print('###################')
    return render(request, 'index.html')

@csrf_protect
def busqueda_normal(request):
    if request.method == 'POST':
        tipo_reserva = request.POST.get("select_tipo_reserva")
        fecha_reserva = request.POST.get("fecha_reserva")
        tipo_habitacion = request.POST.get("select_tipo_habitacion")
        num_adultos = request.POST.get("select_num_adultos")

        print(tipo_reserva)
        print(fecha_reserva)        
        print(tipo_habitacion)
        print(num_adultos)

def prueba(request):
    print('###################')
    print(request.user.id)    
    print(request.user.extra_data)    
    print('###################')
    return render(request, 'prueba.html')
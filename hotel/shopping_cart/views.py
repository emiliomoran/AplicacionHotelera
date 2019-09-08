from django.shortcuts import render
from accesos.models import Cliente,Perfil
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    # print(request.session['nombres'])
    print('cart view')    
    print(request.user.id)    
    print('###################')
    return render(request, 'shopping_cart/index.html')

@login_required(login_url = '/accesos/login/')
def add_to_cart(request,**kwargs):
	user = get_object_or_404(Cliente, user=request.user)

	#Lo siguiente deberia ser considerado como un Producto de manera general, pero por ahora sera un cuarto.
	cuarto = Room.objects.filter(id=kwargs.get('item_id',"")).first()
	perfil = Perfil.objects.filter(usuario=user)

	

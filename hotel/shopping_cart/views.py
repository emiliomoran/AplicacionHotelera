from django.shortcuts import render
from accesos.models import Cliente,Perfil


# Create your views here.
def index(request):
    # print(request.session['nombres'])
    print('cart view')    
    print(request.user.id)    
    print('###################')
    return render(request, 'shopping_cart/index.html')





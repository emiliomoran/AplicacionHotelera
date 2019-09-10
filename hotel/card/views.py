from django.shortcuts import render
from accesos.models import Usr

# Create your views here.
def index(request):
    # print(request.session['nombres'])
    print('card view')    
    print(request.user.username)    
    print('###################')
    return render(request, 'card/index.html', {"uid":request.user.username, "email":request.user.email})
    
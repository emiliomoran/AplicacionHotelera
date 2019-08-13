from django.shortcuts import render

# Create your views here.
def index(request):
    # print(request.session['nombres'])
    print('###################')    
    print(request.user.id)    
    print('###################')
    return render(request, 'index.html')

def prueba(request):
    print('###################')
    print(request.user.id)    
    print(request.user.extra_data)    
    print('###################')
    return render(request, 'prueba.html')
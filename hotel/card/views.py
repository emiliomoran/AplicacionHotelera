from django.shortcuts import render

# Create your views here.
def index(request):
    # print(request.session['nombres'])
    print('card view')    
    print(request.user.id)    
    print('###################')
    return render(request, 'card/index.html')
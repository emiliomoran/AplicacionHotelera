from django.shortcuts import render

# Create your views here.
def index(request):
    # print(request.session['nombres'])
    return render(request, 'index.html')
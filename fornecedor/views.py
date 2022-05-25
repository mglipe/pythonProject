from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def logged(request):
    return render(request, 'userLogged/logged.html')
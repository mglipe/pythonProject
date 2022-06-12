from cgitb import reset
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import PBKDF2PasswordHasher

# Create your views here.

def index(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        print(email)
        print(senha)
        
        if(email == "" or senha == ""):
            print('campo nao pode ficar em branco')
            return redirect('index')

        if User.objects.filter(email= email).exists():
            nome = User.objects.filter(email= email).values_list('username', flat=True).get()    
            print('user registered: ', nome)
            user = auth.authenticate(request, username= nome, password= senha)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            else: 
                print('usuário não cadastrado')
        
    return render(request, 'index.html')


def cadastro(request):
    if request.method == 'POST':
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        

        if not name.strip():
            print("the can't field blank")
            return redirect('cadastro')
        if(User.objects.filter(email= email).exists()):
            print('usuario ja cadastrado!')
            return redirect('cadastro')
        
        user = User.objects.create(username= name, email= email, password= password)
        user.save()
        print('usuario cadastrado com sucesso!')

        return redirect('index')
        
                                                                                                                  
    
    return render(request, 'cadastroUser/index.html')


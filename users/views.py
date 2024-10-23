from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request): # é a resposta do usuario/servidor
    if not request.user.is_authenticated:#já do django
        return HttpResponseRedirect(reverse('login'))#reverse serve para acessar a url pelo nome das urls
    return render(request, 'users/user.html')

def login_view(request):
    if request.method == 'POST': #se o request foi enviado pelo usuario
        username = request.POST['username']#request.post é onde armazena o input
        password = request.POST['password']#no name do input html
        user = authenticate(request, username=username, password=password)
        #se o username == username autentifica
        if user is not None:
            login(request, user)#aqui faz o login do user
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'users/login.html',{
                'message': "Invalid Credentials"
            })

    return render(request, 'users/login.html')

def logout_view(request):
    logout(request)#se for logout
    return render(request, 'users/login.html', {
        'message': "Logged Out"
    })
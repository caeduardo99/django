from ast import If
from curses import use_default_colors


from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html', {
    })


def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()
                return HttpResponse('Usuario registrado exitosamente')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'las contraseñas no coinciden'
        })

@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            "form": AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST
            ['password'])
        if user is None:
            return render(request, 'signin.html', {
                "form": AuthenticationForm, 
                "error": "Username or password is incorrect."
            })
        login(request,user)
        return redirect('home')

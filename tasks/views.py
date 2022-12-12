from ast import If


from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import  TaskForm
from .models import Task
# Create your views here.


#Home
def home(request):
    return render(request, 'home.html', {
    })


#Tasks
def dashboard(request):
    Listar = Task.objects.filter(user=request.user)
    return render(request, 'tasks.html', {'tasks': Listar})


#Crear Tarea
def create_task(request): 
    if request.method == 'GET':
         return render(request, 'create_tasks.html',{
        'form':TaskForm
    })
    else:
        form = TaskForm(request.POST)
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.save()
        return redirect('/tasks')


#Detalle de la Tarea
def task_detail(request,task_id):
    task= get_object_or_404(Task, pk=task_id)
    return render(request, 'task_detail.html',{'task': task})


#Registro Usuario    
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


#Vista protegida
@login_required
def signout(request):
    logout(request)
    return redirect('home')


#Inicio Sesion
def signin(request):
    # Carga el form
    if request.method == 'GET':
        return render(request, 'signin.html', {
            "form": AuthenticationForm
        })
    # Autentifica por POST
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

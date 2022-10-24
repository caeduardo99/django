from curses import use_default_colors
import http
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def hola(request):
    # return HttpResponse('hola mundo') 
   # title= 'hello world'
    return render(request,'signup.html', {
        'form' : UserCreationForm
    })
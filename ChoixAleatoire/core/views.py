from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .forms import UserForm
from .models import *

# Create your views here.
from django.http import HttpResponse

@csrf_exempt
def connexion(request):
    template_name = 'connexion.html'
    if request.method == 'POST':
       nom = request.POST['nom']
       password_nom = request.POST['password']
       test = Profile.objects.all()
       for i in test :
           if i.nom == nom and i.password == password_nom :
                return redirect('home')
           
       messages.error(request , 'Désolé mot de passe ou username incorrect')
       return redirect('connexion')
           
    return render(request ,template_name)

@csrf_exempt
def home(request):
    template_name = 'index.html'
    return render(request , template_name)

@csrf_exempt
def register(request):
    template_name = 'register.html'
    if request.method == 'POST':
        profile = Profile()
        profile.nom = request.POST['nom']
        profile.password = request.POST['password']
        profile.save()
        messages.success(request , "Votre compte a bien été  enregistré")
        return redirect('connexion')

    return render(request , template_name)

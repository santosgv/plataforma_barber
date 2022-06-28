from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    return render(request, 'home.html')

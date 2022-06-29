from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Agendamento
from django.contrib import auth


def agendamentos(request):
    agenda = Agendamento.objects.all().filter(status='A')
    return render(request, 'agendamento.html',{'agenda':agenda})

def agendar(request):
    
    return render(request, 'agendar.html')
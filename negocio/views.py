from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Agendamento ,Horario , Dia ,Funcionario
from django.contrib import auth


def agendamentos(request):
    usuario = request.user
    agenda = Agendamento.objects.all().filter(status='A').filter(usuario=usuario)
    return render(request, 'agendamento.html',{'agenda':agenda})

def agendar(request):
    if request.session.get('GET'):
        return render(request, 'agendar.html')
    else:
        horas = Horario.objects.all()
        dias = Dia.objects.all()
        funcionarios = Funcionario.objects.all()
        
        dia = request.POST.get('dias')
        hora = request.POST.get('hora')
        funcionario = request.POST.get('funcionario')
        usuario = request.user
        
        Agenda = Agendamento(Funcionario = funcionario,
                                    usuario = usuario,
                                    dia = dia,
                                    horario = hora,
                                    )

        Agenda.save()

        return render(request, 'agendar.html',{'dias':dias,
                                                'horas' :horas,
                                                'funcionarios':funcionarios})
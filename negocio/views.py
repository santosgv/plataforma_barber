from os import name
from django.contrib import messages
from django.contrib.messages import constants
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render ,get_object_or_404
from django.contrib.auth.models import User
from .models import Agendamento ,Horario , Dia ,Funcionario
from django.contrib import auth
from django.contrib.auth.decorators import login_required

@login_required(login_url='logar')
def agendamentos(request):
    usuario = request.user
    agenda = Agendamento.objects.all().filter(usuario=usuario)
    return render(request, 'agendamento.html',{'agenda':agenda})

@login_required(login_url='logar')
def agendar(request):

    horas = Horario.objects.all()
    dias = Dia.objects.all()
    funcionarios = Funcionario.objects.all()
    
    return render(request, 'agendar.html',{'dias':dias,
                                            'horas' :horas,
                                            'funcionarios':funcionarios})

@login_required(login_url='logar')
def valida(request):
    dia = request.POST.get('dias')
    hora = request.POST.get('hora')
    funcionario = request.POST.get('funcionario')
    usuario = request.user

    

    if Agendamento.objects.filter(dia=Dia.objects.get(dia=dia)).filter(horario=Horario.objects.get(horario=hora)).filter(Funcionario=Funcionario.objects.get(nome=funcionario)).filter(status='A'):

        messages.add_message(request, constants.ERROR, 'Dia e Horario Ja reservado com este Profissional queira escolher outra data por gentileza !')


        return render(request, 'erro_agendamento.html',{'dia': dia,
                                                        'hora': hora,
                                                        'funcionario' : funcionario
                                                        })

    else:
        Agenda = Agendamento(Funcionario = Funcionario.objects.get(nome=funcionario),
                                    usuario = usuario,
                                    dia = Dia.objects.get(dia=dia),
                                    horario = Horario.objects.get(horario=hora)
                                    )

        Agenda.save()

        agenda = Agendamento.objects.all().filter(usuario=usuario)

        return render(request, 'agendamento.html',{'agenda':agenda})

@login_required(login_url='Login')
def cancela_agendamento(request):
    return   HttpResponse('Cancelado')
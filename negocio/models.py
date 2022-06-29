from django.db import models
from datetime import datetime
from django.db.models.fields import CharField
from django.contrib.auth.models import User

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(blank=True, max_length=18)

    def __str__(self) -> str:
        return str(self.nome)

class Dia(models.Model):
    dia = models.CharField(max_length=20)

    def __str__(self) -> str:
        return str(self.dia)

class Horario(models.Model):
    horario = models.TimeField()

    def __str__(self) -> str:
        return str(self.horario)


class Agendamento(models.Model):
    choices_status = (('A', 'Agendado'),
                      ('F', 'Finalizado'),
                      ('C', 'Cancelado'))

    Funcionario = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dia = models.ForeignKey(Dia ,on_delete=models.DO_NOTHING)
    horario = models.ForeignKey(Horario, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=1, choices=choices_status, default="A")
    observacao = models.TextField(max_length=500 ,blank=True)

    def __str__(self) -> str:
        return str(self.Funcionario)
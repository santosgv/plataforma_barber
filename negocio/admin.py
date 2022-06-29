from django.contrib import admin
from .models import Funcionario, Dia , Horario, Agendamento

admin.site.register(Funcionario)
admin.site.register(Dia)
admin.site.register(Horario)
admin.site.register(Agendamento)
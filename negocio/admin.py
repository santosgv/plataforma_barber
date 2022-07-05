from django.contrib import admin
from .models import Funcionario, Dia , Horario, Agendamento

admin.site.register(Funcionario)

admin.site.register(Dia)

admin.site.register(Horario)

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    readonly_fields = ('Funcionario','usuario','dia','horario',)
    search_fields =('status','Funcionario','dia','horario',)
    list_display = ('status','Funcionario','dia','horario','observacao',)
    list_filter = ('status','Funcionario','dia','horario',)

from . import views
from django.urls import path

urlpatterns = [
    path('agendamento', views.agendamentos, name='agendamento'),
    path('agendar', views.agendar, name='agendar'),
    path('valida', views.valida, name='valida'),
    path('cancela_agendamento/<str:id>', views.cancela_agendamento, name='cancela_agendamento')
]

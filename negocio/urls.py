from . import views
from django.urls import path

urlpatterns = [
    path('/agendamento', views.agendamentos, name='agendamento'),
    path('/agendar', views.agendar, name='agendar'),
]

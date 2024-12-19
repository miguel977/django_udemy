from django.urls import path
from.views import desafio_semana, desafio_semana_numero
urlpatterns = [
    path('<int:dia>', desafio_semana_numero),
    path('<str:dia>', desafio_semana, name='desafio_semana'),
]

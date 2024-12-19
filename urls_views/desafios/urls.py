from django.urls import path
from.views import desafio_semana
urlpatterns = [
    path('<dia>', desafio_semana)
]

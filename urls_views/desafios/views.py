from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def desafio_semana(request, dia):
    desafio=""
    if dia == 'domingo':
        desafio ='Ler Livro sobre Django'
    
    elif dia == 'segunda':
        desafio = 'Assistir Série Breaking Bad'

    elif dia == 'terca':
        desafio = 'Estudar programação Python'

    elif dia == 'quarta':
        desafio = 'Fazer um curso de Design Gráfico'

    elif dia == 'quinta':
        desafio = 'Praticar um Esporte'

    elif dia == 'sexta':
        desafio = 'none'

    elif dia == 'sabado':
        desafio = 'Ir a Igreja'

    else:
        return HttpResponseNotFound("Não há desafio para esse dia informado")
    return HttpResponse(desafio)



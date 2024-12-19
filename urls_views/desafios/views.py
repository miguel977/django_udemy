from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


desafios_dia_semana = {
    'domingo': ' Ler Livro sobre Django',
    'segunda': ' Assistir Série Breaking Bad',
    'terça': ' Estudar programação Python',
    'quarta': ' Fazer um curso de Design Gráfico',
    'quinta': ' Praticar um Esporte',
    'sexta': ' fazer um projeto voluntário',
    'sábado': ' Ir a Igreja'
} 

def desafio_semana_numero(request, dia):
    dias = list(desafios_dia_semana.keys())
    if dia > len(dias) or dia == 0: 
        return HttpResponseNotFound("Dia inválido")
    dia_escolhido = dias[dia - 1]
    return HttpResponseRedirect("/desafios/" + dia_escolhido)
    redireciona_rota = reverse("desafio_semanal", args=[dia_escolhido])
    return HttpResponseRedirect(redireciona_rota)
def desafio_semana(request, dia):
    try:
        desafio = desafios_dia_semana[dia],
    except:
        return HttpResponseNotFound("Para esse parâmetro não há desafio")
    return HttpResponse(desafio)


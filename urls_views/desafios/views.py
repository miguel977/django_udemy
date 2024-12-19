from django.shortcuts import render
from django.http import HttpResponse

def domingo(request):
    return HttpResponse("Ler Livro sobre Django")

def segunda(request):
    return HttpResponse('Assistir Série Breaking Bad')

def terca(request):
    return HttpResponse('Estudar programação Python')

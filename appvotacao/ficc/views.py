from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home(request):

    return render(request, 'home.html')

def opcoes(request):

    return render(request, 'opcoes.html')


def votofeminino(request):

    return render(request, 'votofeminino.html')

def votodemenores(request):

    return render(request, 'votodemenores.html')

def votodeanalfabetos(request):

    return render(request, 'votodeanalfabetos.html')

def votodenegros(request):

    return render(request, 'votodenegros.html')

def votobranconulo(request):

    return render(request, 'votobranconulo.html')

def votodecabresto(request):

    return render(request, 'votodecabresto.html')

def aprovacao(request, voto):
    if voto == "votofeminino":
        aux = VotoFeminino(votofeminino=+1)
        aux.save()

    if voto == "votodemenores":
        aux = VotoDeMenores(votodemenores=+1)
        aux.save()

    if voto == "votodeanalfabetos":
        aux = VotoDeAnalfabetos(votodeanalfabetos=+1)
        aux.save()

    if voto == "votodenegros":
        aux = VotoDeNegros(votodenegros=+1)
        aux.save()

    if voto == "votobranconulo":
        aux = VotoBrancoNulo(votobranconulo=+1)
        aux.save()

    if voto == "votodecabresto":
        aux = VotoDeCabresto(votodecabresto=+1)
        aux.save()

    if voto == "aprovou":
        aux = VotoAprovou(aprovou=+1)
        aux.save()
        return redirect('/opcoes')

    if voto == "naoaprovou":
        aux = VotoNaoAprovou(naoaprovou=+1)
        aux.save()
        return redirect('/opcoes')

    return render(request, 'aprovacao.html')

def dashboard(request):
    votofeminino = VotoFeminino.objects.all().count()
    votodemenores = VotoDeMenores.objects.all().count()
    votodeanalfabetos = VotoDeAnalfabetos.objects.all().count()
    votodenegros = VotoDeNegros.objects.all().count()
    votobranconulo = VotoBrancoNulo.objects.all().count()
    votodecabresto = VotoDeCabresto.objects.all().count()
    aprovou = VotoAprovou.objects.all().count()
    naoaprovou = VotoNaoAprovou.objects.all().count()

    return render(request, 'dashboard.html', {'naoaprovou':naoaprovou,'aprovou':aprovou ,'votofeminino': votofeminino, 'votodemenores': votodemenores, 'votodeanalfabetos': votodeanalfabetos, 'votodenegros': votodenegros, 'votobranconulo':votobranconulo, 'votodecabresto':votodecabresto})
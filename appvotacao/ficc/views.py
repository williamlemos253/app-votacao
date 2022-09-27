from django.shortcuts import render

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
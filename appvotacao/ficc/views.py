from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'home.html')

def opcoes(request):

    return render(request, 'opcoes.html')


def votofeminino(request):

    return render(request, 'votofeminino.html')
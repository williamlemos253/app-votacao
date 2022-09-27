from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('opcoes', views.opcoes),
    path('votofeminino', views.votofeminino)
    ]
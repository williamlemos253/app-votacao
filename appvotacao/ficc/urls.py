from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('opcoes', views.opcoes),
    path('votofeminino', views.votofeminino),
    path('votodemenores', views.votodemenores),
    path('votodeanalfabetos', views.votodeanalfabetos),
    path('votodenegros', views.votodenegros),
    path('votobranconulo', views.votobranconulo),
    path('votodecabresto', views.votodecabresto),
    ]
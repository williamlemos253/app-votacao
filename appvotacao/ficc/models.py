from django.db import models

# Create your models here.

class VotoFeminino(models.Model):
    votofeminino = models.PositiveIntegerField()

class VotoDeMenores(models.Model):
    votodemenores = models.PositiveIntegerField()

class VotoDeAnalfabetos(models.Model):
    votodeanalfabetos = models.PositiveIntegerField()

class VotoDeNegros(models.Model):
    votodenegros = models.PositiveIntegerField()

class VotoBrancoNulo(models.Model):
    votobranconulo = models.PositiveIntegerField()

class VotoDeCabresto(models.Model):
    votodecabresto = models.PositiveIntegerField()

class VotoAprovou(models.Model):
    aprovou = models.PositiveIntegerField()

class VotoNaoAprovou(models.Model):
    naoaprovou = models.PositiveIntegerField()

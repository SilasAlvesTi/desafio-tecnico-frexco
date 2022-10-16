from django.db import models


class Usuario(models.Model):
    login = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=50, blank=True)
    data_nascimento = models.DateField(max_length=8)
    criado_em = models.DateField(auto_now_add=True)

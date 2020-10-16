from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True, null=True)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d')
    login = models.IntegerField(default=0)
    desafio_id = models.IntegerField(default=0)
    sql_desafio = models.IntegerField(default=0)
    new_code = models.CharField(max_length=350, default='dsadsadsadadgfdg', blank=True)
    new_senha = models.CharField(max_length=350, default='123456', blank=True, null=True)
    new_header = models.CharField(max_length=350, default='', blank=True, null=True)
    new_header2 = models.CharField(max_length=350, default='', blank=True, null=True)

def __str__(self):
        return self.nome




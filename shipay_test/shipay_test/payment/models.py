from django.db import models


class Estabelecimento(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=20)
    dono = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)


class Recebimentos(models.Model):
    Estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)
    cliente = models.CharField(max_length=20)
    valor = models.FloatField()
    descricao = models.CharField(max_length=255)
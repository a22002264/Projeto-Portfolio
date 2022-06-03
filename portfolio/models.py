from django.db import models


# Create your models here.
# models.py

class Linguagem(models.Model):
    nome = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.nome}"


class Projeto(models.Model):
    nome = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.nome}"


class Cadeira(models.Model):
    nome = models.CharField(max_length=100)
    ano = models.IntegerField()
    descricao = models.TextField()
    linguagens = models.ManyToManyField(Linguagem)
    projetos = models.ManyToManyField(Projeto)

    def _str_(self):
        return f"{self.nome}"

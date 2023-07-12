from django.db import models
from django.utils import timezone


LISTA_CATEGOTIAS = (
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)
class Filme(models.Model):
    titulo =models.CharField(max_length=100)
    thumb = models.ImageField(upload_to='thumb_filmes')
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGOTIAS)
    vizualizacoes = models.IntegerField(default=0)
    data_criação = models.DateField(default=timezone.now)

    def __str__(self):
        return self.titulo
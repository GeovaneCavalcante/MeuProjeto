from django.db import models
from django.utils import timezone
from PIL import Image


class Postagens(models.Model):
    autor = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data_publicada = models.DateField(default=timezone.now())
    imagem = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.titulo

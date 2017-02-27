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

class formss(models.Model):
    email = models.EmailField(max_length=100)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()

    def __str__(self):
        return self.titulo

class Carosel(models.Model):
    titulo_carosel = models.CharField(max_length=50)
    texto_carosel = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return self.titulo_carosel
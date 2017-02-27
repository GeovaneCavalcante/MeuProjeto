from django import forms

class Meu_From(forms.Form):
    email = forms.CharField(label='Your name', max_length=100)
    titulo = forms.CharField(label='Titulo', max_length=100)
    texto = forms.CharField(label='Texto', max_length=500)
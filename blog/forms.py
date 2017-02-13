from django import forms

class Meu_Form(forms.Form):
    titulo = forms.CharField(label='titulo', max_length=50)
    texto = forms.CharField(label='texto', max_length=1000)
    email = forms.CharField(label='email', max_length=30)

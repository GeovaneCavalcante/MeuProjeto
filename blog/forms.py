from django import forms

class MeuForm(forms.Form):
    titulo = forms.CharField(label='titulo', max_length=50)
    texto = forms.CharField(label='texto', max_length=400)
    email = forms.CharField(label='email', max_length=300)


from django import forms

class MeuForm(forms.Form):
    titulo = forms.CharField(label='novo', max_length=50)



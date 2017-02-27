from django.shortcuts import render, loader, get_object_or_404
from .models import Postagens, Carosel, formss
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .forms import Meu_From

def index(request):
    lista_postagem = Postagens.objects.order_by('-data_publicada')[:6]
    carosel_posta = Carosel.objects.all()
    form = Formulario(request, Meu_From)
    context = {
        'lista_postagem': lista_postagem,
        'carosel_posta': carosel_posta,
        'form':form,
    }
    return render(request, 'blog/index.html', context)

def Formulario(request, Meu_form):
    if request.method == 'POST':
        form = Meu_From(request.POST)
        if form.is_valid():
            q = formss()
            q.titulo = form.data.get('titulo')
            q.texto = form.data.get('texto')
            q.email = form.data.get('email')
            q.save()
            return HttpResponseRedirect('/index/')
    else:
        form = Meu_From()
    return (request, form)

def resultados(request, postagens_id):
    postagenss = get_object_or_404(Postagens, pk=postagens_id)
    return render(request, 'blog/restultados.html', {'postagenss': postagenss})

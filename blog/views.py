from django.shortcuts import render, loader, get_object_or_404
from .models import Postagens, Carosel, Enviados
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .forms import MeuForm

def index(request):
    lista_postagem = Postagens.objects.order_by('-data_publicada')[:5]
    carosel_posta = Carosel.objects.all()
    context = {
        'lista_postagem': lista_postagem,
        'carosel_posta': carosel_posta,
    }
    return render(request, 'blog/index.html', context)

def get_name(request):
    if request.method == 'POST':
        form = MeuForm(request.POST)
        if form.is_valid():
            q = Enviados()
            q.email = form.data.get('email')
            q.titulo = form.data.get('titulo')
            q.texto = form.data.get('texto')
            q.save()
            return HttpResponseRedirect('/resultados/')
    else:
        form = MeuForm()

    return render(request, 'blog/index.html', {'form': form})


def resultados(request, postagens_id):
    postagenss = get_object_or_404(Postagens, pk=postagens_id)
    return render(request, 'blog/restultados.html', {'postagenss': postagenss})

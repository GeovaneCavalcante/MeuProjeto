from django.shortcuts import render, loader, get_object_or_404
from .models import Postagens


def index(request):
    lista_postagem = Postagens.objects.order_by('-data_publicada')[:5]
    context = {
        'lista_postagem': lista_postagem,
    }
    return render(request, 'blog/index.html', context)


def resultados(request, postagens_id):
    postagenss = get_object_or_404(Postagens, pk=postagens_id)
    return render(request, 'blog/restultados.html', {'postagenss': postagenss})

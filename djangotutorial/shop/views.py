from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Artigo, Categoria, Vendedor


def lista_artigos(request):
    artigos = Artigo.objects.all()
    return render(request, 'shop/lista_artigos.html', {'artigos': artigos})


def artigos_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    artigos = Artigo.objects.filter(categoria=categoria)
    return render(request, 'shop/artigos_por_categoria.html', {
        'categoria': categoria,
        'artigos': artigos
    })


def perfil_vendedor(request, vendedor_id):
    vendedor = get_object_or_404(Vendedor, id=vendedor_id)
    artigos = Artigo.objects.filter(vendedor=vendedor)
    return render(request, 'shop/perfil_vendedor.html', {
        'vendedor': vendedor,
        'artigos': artigos
    })
# Create your views here.

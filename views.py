from django.shortcuts import render
from .models import Cadastro1

def primeiraPagina(request):
    cadastros = Cadastro1.objects.all()

    return render(request, 'cadastro/home.html',{'cadastros' : cadastros })

def pagina2(request, clique_mouse):
    ver_descricao = Cadastro1.objects.get(id=clique_mouse)
    return render(request, 'cadastro/visualizar.html', {'ver_descricao': ver_descricao })
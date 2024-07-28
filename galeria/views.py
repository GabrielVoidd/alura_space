from django.shortcuts import render

# Create your views here.


def index(request):
    # quando chegar uma requisição para o index, responda de acordo com o return
    return render(request, 'galeria/index.html')


def imagem(request):
    return render(request, 'galeria/imagem.html')

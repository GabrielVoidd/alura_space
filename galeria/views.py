from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # quando chegar uma requisição para o index, responda de acordo com o return
    return HttpResponse(
        '<h1>Hello World</h1>'
        '<p>Agora funcionou</p>'
    )

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<a href='special'>Special</a><br><a href='pontos'>pontos</a><br><a href='bacon'>bacon</a><br><strong>Coé</strong>")

def special(request):
    context = {
        "nome":"Luque",
        "nome_familia":"truco"
    }
    return render(request,"treuke/truco.html", context)

def pontos(request):
    return render(request,"treuke/exercicio_pontos.html")

def bacon(request):
    return render(request,"treuke/bacon.html")
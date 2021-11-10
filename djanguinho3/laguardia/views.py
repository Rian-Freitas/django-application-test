from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

def redireciona(request):
    url = reverse("trickortreat")
    return HttpResponseRedirect(url)

def index(request):
    return HttpResponse("<h1>🦇Mwhaha! Seja bem-vindo a minha página mal assombrada!🦇</h1>\
    <br>Procure por personagens de halloween no link.🎃")

def trickortreat(request):
    context = {"possib" : ['🍬 você achou um doce :D', '😈 você foi trickado >:D haha']}
    return render(request, "laguardia/trickortreat.html", context)


def dracula(request):
    return render(request, "laguardia/dracula.html")

def mumia(request):
    return render(request, "laguardia/mumia.html")

def fantasma(request):
    return render(request, "laguardia/fantasma.html")

def custom(request):
    context = {"criatura": "👾",
                "frase1": "~Digite aqui a frase principal~",
                "frase2": "~Digite aqui a frase secundária~",
                "atributos": ["Força: 5", "Inteligência: 7", "Destreza: 2", "Lábia: 4", "Velocidade: 3"]}

    return render(request, "laguardia/custom.html", context)

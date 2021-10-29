from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>🦇Mwhaha! Seja bem-vindo a minha página mal assombrada!🦇</h1>\
    <br>Procure por personagens de halloween no link.🎃")

def treat(request):
    return HttpResponse("🍬 você achou um doce :D")


def dracula(request):
    return render(request, "laguardia/dracula.html")

def mumia(request):
    return render(request, "laguardia/mumia.html")

def fantasma(request):
    return render(request, "laguardia/fantasma.html")
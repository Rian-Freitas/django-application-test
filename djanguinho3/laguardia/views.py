from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound

def redireciona(request):
    url = reverse("trickortreat", args=["treat"])
    return HttpResponseRedirect(url)

def index(request):
    return HttpResponse("<h1>🦇Mwhaha! Seja bem-vindo a minha página mal assombrada!🦇</h1>\
    <br>Procure por personagens de halloween no link.🎃")

def trickortreat(request, choice):
    if choice == "treat":
        return HttpResponse("🍬 você achou um doce :D")
    elif choice == "trick":
        return HttpResponse("😈 você foi trickado >:D haha")
    else:
        return HttpResponseNotFound("Escolha inválida :c")


def dracula(request):
    return render(request, "laguardia/dracula.html")

def mumia(request):
    return render(request, "laguardia/mumia.html")

def fantasma(request):
    return render(request, "laguardia/fantasma.html")

def custom(request):
    context = {"criatura": "👾",
                "frase1": "~Digite aqui a frase principal~",
                "frase2": "~Digite aqui a frase secundária~"}

    return render(request, "laguardia/custom.html", context)

from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404

def redireciona(request):
    url = reverse("trickortreat")
    #return HttpResponseRedirect(url)

    #agora o redireciona vai dar erro 404
    raise Http404()

def index(request):
    return HttpResponse("""<h1>🦇Mwhaha! Seja bem-vindo a minha página mal assombrada!🦇</h1><br>
    <br>
    <h2>Páginas disponíveis:</h2> <br>
    <a href="dracula">Drácula</a> <br>
    <a href="fantasma">Fantasma</a> <br>
    <a href="mumia">Múmia</a> <br>
    <a href="custom/frase1/frase2">Custom</a> <br>
    <a href="trickortreat">Trick or Treat</a> <br>
    """)

def trickortreat(request):
    context = {"possib" : ['🍬 você achou um doce :D', '😈 você foi trickado >:D haha']}
    return render(request, "laguardia/trickortreat.html", context)


def dracula(request):
    return render(request, "laguardia/dracula.html")

def mumia(request):
    return render(request, "laguardia/mumia.html")

def fantasma(request):
    return render(request, "laguardia/fantasma.html")

def custom(request, frase1, frase2):
    context = {"criatura": "👾",
                "frase1": frase1.replace("_", " "),
                "frase2": frase2.replace("_", " "),
                "atributos": ["Força: 5", "Inteligência: 7", "Destreza: 2", "Lábia: 4", "Velocidade: 3"]}

    return render(request, "laguardia/custom.html", context)

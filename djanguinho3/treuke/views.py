from django.http import HttpResponse, Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse

# Create your views here.
def index(request):
    return render(request,"treuke/truco-index.html")

def redireciona(request):
    url = reverse("bacon")
    return HttpResponseRedirect(url)

def view_dinamica_int(request,param):
    if param == 0:
        return HttpResponse("<strong>ALO</strong>")
    elif param == 1:
        return HttpResponse("<strong>ALO2</strong>")
    else:
        raise Http404()


def special(request):
    return render(request,"treuke/truco.html")

def pontos(request):
    return render(request,"treuke/exercicio_pontos.html")

def bacon(request):
    context = {
        "nome":"samplenamehere",
        "list":["a","b","c"],
        "string_espacada":"AA    aaa  loo oo",
        "valor":""
    }
    return render(request,"treuke/bacon.html",context)

def templario(request):
    return render(request,"treuke/templario.html")
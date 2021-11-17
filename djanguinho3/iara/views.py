from django.http.response import HttpResponseNotFound
from django.http.response import Http404
from django.shortcuts import render, reverse
from django.http import HttpResponse

def index(request):
    return render(request, "iara/iara.html")

def error(request):
    raise Http404()

def special(request):
    context = {
        "nome":"Iara",
        "nome_familia":"Cristina"
    }
    return render(request,"iara/iara.html", context)

def view_dinamica_int(request, param):
    if param == 0:
        return HttpResponse("<strong> Parâmentro 0 </strong>")
    if param == 1:
        return HttpResponse("<strong> Parâmentro 1 </strong>")
    if param == 2:
        return HttpResponse("<strong> Parâmentro 2 </strong>")
    else:
        raise Http404()


def halloween(request):
    return render(request,"iara/halloween.html")

def caraoucoroa(request):
    context = {"possib" : ['Cara', 'Coroa']}
    return render(request, "iara/caracoroa.html", context)

def frasemotivacional(request):
    return render(request,"iara/frasemotivacional.html")

# Create your views here.

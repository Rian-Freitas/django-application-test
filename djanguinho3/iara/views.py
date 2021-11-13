from django.http.response import HttpResponseNotFound
from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "iara/iara.html")

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


def special_2(request):
    return render(request,"iara/teste2.html")

def special_3(request):
    return render(request,"iara/iara_template.html")

def caraoucoroa(request):
    context = {"possib" : ['Cara', 'Coroa']}
    return render(request, "iara/caracoroa.html", context)
# Create your views here.

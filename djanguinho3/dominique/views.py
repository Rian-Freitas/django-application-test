from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse
import random

# Create your views here.
def index(request):
    return HttpResponse("<strong>AAAAAAAAAAA</strong>")

def view_dinamica_int(request,param):
    if param == 0:
        return HttpResponse("<strong>Sei lá</strong>")
    elif param == 1:
        return HttpResponse("<strong>Sei lá 2</strong>")

def special(request):
    return render(request,"Domi/index.html")

def index_2(request):
    return render(request,"Domi/index_2.html")

def index_3(request):
    respostas = ["sim", "não"]
    context = {
        "nome":"Dominique",
        "lista":["Treuke", "Laguardia", "Rodrigo", "Iara", "Rian"],
        "resposta":random.choice(respostas),
        "res1":"que bom!",
        "res2":"f por você.",
    }
    return render(request,"Domi/index_3.html", context)

def redireciona(request):
    url = reverse(index_3)
    return HttpResponseRedirect(url)
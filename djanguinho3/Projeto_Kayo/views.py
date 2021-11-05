# from django.shortcuts import render
# ^^ isso aqui ja tinha antes ^^

from django.http import HttpResponse
from django.shortcuts import render 

# Create your views here.

def index(request):
    return HttpResponse("<strong>Primeira Página</strong>")

def infograf(request):
    context = {
        "nome":"Kayo",
        "nome_familia":"Torto"
    }
    return render(request,"Projeto_Kayo/infograficos_kurzgesagt.html", context)

def desenho_1(request):
    return render(request,"Projeto_Kayo/desenho_1.html")

def desenho_2(request):
    return render(request,"Projeto_Kayo/desenho_2.html")

def desenho_3(request):
    return render(request,"Projeto_Kayo/desenho_3.html")

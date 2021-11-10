from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<strong>olá</strong>")

def special(request):
    context = {
        "nome":"Iara",
        "nome_familia":"Cristina"
    }
    return render(request,"iara/iara.html", context)

def special_2(request):
    return render(request,"iara/teste2.html")

def special_3(request):
    return render(request,"iara/iara_template.html")

def caraoucoroa(request):
    context = {"possib" : ['Cara', 'Coroa']}
    return render(request, "iara/caracoroa.html", context)
# Create your views here.

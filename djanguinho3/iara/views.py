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

# Create your views here.

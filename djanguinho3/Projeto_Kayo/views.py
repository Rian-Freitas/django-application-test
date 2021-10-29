# from django.shortcuts import render
# ^^ isso aqui ja tinha antes ^^

from django.http import HttpResponse
from django.shortcuts import render 

# Create your views here.

def index(request):
    return HttpResponse("<strong>Primeira Página</strong>")

def special(request):
    return render(request, "Projeto_Kayo/infograficos_kurzgesagt.html")

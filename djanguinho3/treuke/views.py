from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<strong>Coé</strong><img src='https://baconmockup.com/300/200' alt='Bacon'>")

def special(request):
    context = {
        "nome":"Luque",
        "nome_familia":"truco"
    }
    return render(request,"treuke/truco.html", context)
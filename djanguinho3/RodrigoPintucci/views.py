from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("<strong>Testando</strong>")

def special(request):
    context = {
        "nome":"Rodrigo",
        "nome_familia":"Pintucci"
    }
    return render(request,"RodrigoPintucci/SVGdesenho2.html", context)
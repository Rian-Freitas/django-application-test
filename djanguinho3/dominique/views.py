from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<strong>AAAAAAAAAAA</strong>")

def special(request):
    context = {
        "nome":"Dominique",
        "nome_familia":"Azevedo"
    }
    return render(request,"dominique/index.html", context)
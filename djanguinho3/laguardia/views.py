from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("sinta-se em casa, só n repara a bagunça")

def chaotic(request):
    return HttpResponse("chegai mermao, se liga na bagunça q zika")

def evil(request):
    return HttpResponse("não sinta-se em casa mwhahahah")

def special(request):
    context = {
        "nome":"Laguardia",
        "sobrenome":""
    }

    return render(request, "laguardia/index.html", context")
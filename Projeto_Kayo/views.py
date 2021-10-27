# from django.shortcuts import render
# ^^ isso aqui ja tinha antes ^^

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<strong>FGV</strong>")

from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import reverse

# Create your views here.
def index(request):
    htmlres = """
    " 🏠 Olá, seja bem vindo :) 🏠 "<br>
    <ul>
    <li><a href='laguardia'> ␊ laguardia</a></li>
    <li><a href='RodrigoPintucci'> 🦐 RodrigoPintucci</a></li>
    <li><a href='treuke'> 🂡 treuke</a></li>
    <li><a href='Rian'> 🤫 Rian</a></li>
    <li><a href='kayo'> ⚰️ kayo</a></li>
    <li><a href='dominique'> 🚗 dominique</a></li>
    <li><a href='iara'> 🧜‍♀️ iara</a></li>
    </ul>
    """
    return HttpResponse(htmlres)

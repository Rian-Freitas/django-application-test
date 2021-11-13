from django.shortcuts import render, reverse
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Minha aplicação é só pra dizer que a Lorde é perfeita</h1>")

def Pure_Heroine(request):
    context = {"musicas" : ['Tennis Court','400 Lux', 'Royals', 'Ribs','Buzzcut Season', 'Team', 'Glory and Gore', 'Still Sane', 'White Teeth Teens', 'A World Alone']}
    return render(request, "Rian/Pure_Heroine.html", context)

def Melodrama(request):
    context = {"musicas" : ['Green Light','Sober', 'Homemade Dynamite', 'The Louvre','Liability', 'Hard Feelings / Loveless', 'Sober II (Melodrama)', 'Writer In The Dark','Supercut', 'Liability (Reprise)', 'Perfect Places']}
    return render(request, "Rian/Melodrama.html", context)

def Solar_Power(request):
    context = {"musicas" : ['The Path','Solar Power', 'California', 'Stoned at the Nail Salon','Fallen Fruit', 'Secrets from a Girl (Who´s Seen It All)', 'The Man with the Axe', 'Dominoes', 'Big Star', 'Leader of a New Regime', 'Mood Ring', 'Oceanic Feeling']}
    return render(request, "Rian/Solar_Power.html", context)
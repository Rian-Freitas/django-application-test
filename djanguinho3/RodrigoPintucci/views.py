from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, reverse

# Create your views here.
def index(request):
    return render(request,"RodrigoPintucci/RPindex.html")

def special(request):
    context = {
        "nome":"Rodrigo",
        "nome_familia":"Pintucci"
    }
    return render(request,"RodrigoPintucci/SVGdesenho2.html", context)

def ferias(request):
    return render(request,"RodrigoPintucci/paginahtml.html")

def cookie(request):
    return render(request,"RodrigoPintucci/cookieborgar.html")

def cookie_din(request, param):
    if param == "acabou":
        return HttpResponse("<strong>VOCÊ COMEU TUDO!!</strong>")
    else:
        raise Http404()

def redireciona(request):
    url_redirecionamento = reverse("cookie_din", args=["acabou"])
    return HttpResponseRedirect(url_redirecionamento)

def cookintucci(request):
    context = {
        "nome":"Rodrigo",
        "nome_familia":"Pintucci"
    }
    return render(request,"RodrigoPintucci/cookieborgar2.html", context)

def ferias_din(request, param):
    if param == "criptografia":
        context = {"crypto" : ['a -> r', 'b -> n','c -> o', 'd -> a', 'e -> h', 'f -> s', 'g -> t', 'h -> e', 'i -> l', 'j -> d', 'k -> v', 'l -> c'],
        "segredo":"redacted",
        "mensagem": "bdc cieh dgadf jh kclh"}
        return render(request,"RodrigoPintucci/criptografia.html", context)   
    else:
        raise Http404() 
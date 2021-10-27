from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<strong>Coé</strong><img src='https://baconmockup.com/300/200' alt='Bacon'>")
from django.contrib import admin
from django.urls import path
from laguardia import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dracula", views.dracula, name="dracula"),
    path("mumia", views.mumia, name="mumia"),
    path("fantasma", views.fantasma, name="gasparzinho"),
    path("custom/<str:frase1>/<str:frase2>", views.custom, name="custom"),
    path("trickortreat", views.trickortreat, name="trickortreat"),
    path("naosei", views.redireciona, name="redirecionado")
]
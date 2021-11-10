from django.contrib import admin
from django.urls import path
from treuke import views as treuke_views


urlpatterns = [
    path("", treuke_views.index, name="index"),
    path("special/", treuke_views.special, name="special"),
    path("pontos/", treuke_views.pontos, name="pontos"),
    path("bacon/", treuke_views.bacon, name="bacon"),
    path("redireciona/",treuke_views.redireciona, name="redireciona"),
    path("special/<int:param>", treuke_views.view_dinamica_int, name="dinamica-int"),
    path("templario",treuke_views.templario, name="templario")
]

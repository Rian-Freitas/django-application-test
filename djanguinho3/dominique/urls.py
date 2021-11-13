from django.contrib import admin
from django.urls import path
from dominique import views

urlpatterns = [
    path("", views.index, name="index"),
    path("special/", views.special, name="special"),
    path("index_2/", views.index_2, name="index_2"),
    path("index_3/", views.index_3, name="index_3"),
    path("redireciona/", views.redireciona, name="redireciona"),
    path("special/<int:param>", views.view_dinamica_int, name="dinamica-int")
]
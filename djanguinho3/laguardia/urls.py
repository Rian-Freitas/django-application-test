from django.contrib import admin
from django.urls import path
from laguardia import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chaotic", views.chaotic, name="chaotic"),
    path("evil", views.evil, name="evil"),
    path("special/", views.special, name="special")
]
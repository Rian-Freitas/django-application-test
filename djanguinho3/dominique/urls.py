from django.contrib import admin
from django.urls import path
from dominique import views

urlpatterns = [
    path("", views.index, name="index")
    path("special/", views.special, name="special")
]
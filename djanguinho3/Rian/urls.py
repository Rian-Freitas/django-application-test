from django.contrib import admin
from django.urls import path
from Rian import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pure_heroine", views.Pure_Heroine, name="pure_heroine"),
    path("melodrama", views.Melodrama, name="melodrama"),
    path("solar_power", views.Solar_Power, name="solar_power")
]
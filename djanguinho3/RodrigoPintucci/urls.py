from django.contrib import admin
from django.urls import path
from RodrigoPintucci import views as RodrigoPintucci_views

urlpatterns = [
    path("", RodrigoPintucci_views.index, name="index"),
    path("special/", RodrigoPintucci_views.special, name="special"),
    path("ferias/", RodrigoPintucci_views.ferias, name="ferias"),
    path("cookie/", RodrigoPintucci_views.cookie, name="cookie")
]
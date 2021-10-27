from django.contrib import admin
from django.urls import path
from RodrigoPintucci import views as RodrigoPintucci_views

urlpatterns = [
    path("", RodrigoPintucci_views.index, name="index")
]
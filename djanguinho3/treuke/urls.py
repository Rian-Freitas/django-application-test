from django.contrib import admin
from django.urls import path
from treuke import views as treuke_views


urlpatterns = [
    path("", treuke_views.index, name="index"),
    path("special/", treuke_views.special, name="special")
]

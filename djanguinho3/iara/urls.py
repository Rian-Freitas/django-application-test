from django.contrib import admin
from django.urls import path
from iara import views as iara_views

urlpatterns = [
    path("", iara_views.index, name="index")
]
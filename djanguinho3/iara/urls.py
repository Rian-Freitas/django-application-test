from django.contrib import admin
from django.urls import path
from iara import views as iara_views

urlpatterns = [
    path("", iara_views.index, name="index"),
    path("special/", iara_views.special, name="special"),
    path("halloween/", iara_views.halloween, name="halloween"),
    path("caraoucoroa", iara_views.caraoucoroa, name="caraoucoroa"),
    path("frasemotivacional", iara_views.frasemotivacional, name="frasemotivacional"),
    path("redirecionar", iara_views.error, name="erro")
]
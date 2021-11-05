from django.contrib import admin
from django.urls import path
from iara import views as iara_views

urlpatterns = [
    path("", iara_views.index, name="index"),
    path("special/", iara_views.special, name="special"),
    path("special_2/", iara_views.special_2, name="special_2"),
    path("special_2/", iara_views.special_3, name="special_3")
]
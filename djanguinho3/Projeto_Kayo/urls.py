"""Projeto_Kayo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Projeto_Kayo import views as Projeto_views

urlpatterns = [
    path("", Projeto_views.index, name = "main_view"),
    path("infograf/", Projeto_views.infograf, name = "infograf"),
    path("desenho_1/", Projeto_views.desenho_1, name = "desenho_1"),
    path("desenho_2/", Projeto_views.desenho_2, name = "desenho_2"),
    path("desenho_3/", Projeto_views.desenho_3, name = "desenho_3")
]
"""djanguinho3 URL Configuration

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
from django.urls import include, path
# from fgv import views as fgv_views
  
urlpatterns = [
    path(r'laguardia/', include('laguardia.urls')),
    path(r"RodrigoPintucci/", include("RodrigoPintucci.urls")), #proibido mudar
    path(r"treuke/",include("treuke.urls")),
    path(r"kayo/", include("Projeto_Kayo.urls")),
    path(r"dominique/", include("dominique.urls")),
    path('admin/', admin.site.urls),
    # path('', fgv_views.index, name="index"),
]

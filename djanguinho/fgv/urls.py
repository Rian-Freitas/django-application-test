from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(r"fgv/", include("fgv.urls")),
    path('admin/', admin.site.urls),
]

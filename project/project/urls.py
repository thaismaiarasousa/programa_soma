from django.contrib import admin
from django.urls import path
from myapp.views import home, somar, lista_somas

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("soma/", somar, name='soma'),
    path("lista_somas/", lista_somas, name='lista_somas'),
]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('soma/', views.somar, name='soma'),
    path('lista_somas/', views.lista_somas, name='lista_somas'),
]

from django.urls import path

from . import views

app_name = 'operaciones'

urlpatterns = [
    # ex: /operaciones/
    path('', views.index, name='index'),
    path('resultado', views.resultado, name='resultado'),
]

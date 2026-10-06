from django.urls import path

from . import views

app_name = 'cilindro'

urlpatterns = [
    # ex: /cilindro/
    path('', views.index, name='index'),
    path('calcular', views.calcular, name='calcular'),
]

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='inicio.html'), name='inicio'),
    path('encuesta/', include('encuesta.urls')),
    path('operaciones/', include('operaciones.urls')),
    path('cilindro/', include('cilindro.urls')),
    path('admin/', admin.site.urls),
]

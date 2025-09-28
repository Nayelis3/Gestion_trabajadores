from django.urls import path
from .views import CargarMultiplesArchivosView

urlpatterns = [
    path('trabajador/<int:pk>/documentos', CargarMultiplesArchivosView.as_view(), name='cargar_documentos'),
]
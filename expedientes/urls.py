from django.urls import path
from .views import CargarMultiplesArchivosView, TrabajadorDetailView

urlpatterns = [
    path('trabajador/<int:pk>/documentos', CargarMultiplesArchivosView.as_view(), name='cargar_documentos'),
    path('trabajador/<int:pk>/', TrabajadorDetailView.as_view(), name='detalle_trabajador'),
]
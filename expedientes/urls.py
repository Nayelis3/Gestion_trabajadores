from django.urls import path
from .views import (
    CargarMultiplesArchivosView,
    TrabajadorDetailView,
    TrabajadorListView,
    TrabajadorCreateView,
    TrabajadorUpdateView,
    TrabajadorDeleteView,
    DocumentoDeleteView
)

urlpatterns = [
    #agregando todas las urls para las vistas
    path('', TrabajadorListView.as_view(), name='lista_trabajadores'),
    path('trabajador/nuevo/', TrabajadorCreateView.as_view(), name="crear_trabajador"),
    path('trabajador/<int:pk>/documentos', CargarMultiplesArchivosView.as_view(), name='cargar_documentos'),
    path('trabajador/<int:pk>/', TrabajadorDetailView.as_view(), name='detalle_trabajador'),
    path('trabajador/<int:pk>/editar/', TrabajadorUpdateView.as_view(), name='editar_trabajador'),
    path('trabajador/<int:pk>/eliminar/', TrabajadorDeleteView.as_view(), name='eliminar_trabajador'),
    path('documento/<int:pk>/eliminar/', DocumentoDeleteView.as_view(), name='eliminar_documento'),

]
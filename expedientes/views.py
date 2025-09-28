from django.shortcuts import render
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, redirect
from .models import Trabajador, Documento
from .forms import  CargarMultiplesArchivosForm

class CargarMultiplesArchivosView(FormView):
    template_name = "expedientes/cargar_documentos.html"
    form_class = CargarMultiplesArchivosForm

    def form_valid(self, form):
        trabajador_id = self.kwargs['pk']
        trabajador = get_object_or_404(Trabajador, pk=trabajador_id)
        archivos = form.cleaned_data['archivos']
        for archivo in archivos:
            Documento.objects.create(trabajador=trabajador, archivo=archivo)
        return redirect("detalle_trabajador", pk=trabajador_id)
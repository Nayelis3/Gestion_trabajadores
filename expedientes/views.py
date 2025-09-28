from django.shortcuts import render
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404, redirect
from .models import Trabajador, Documento
from .forms import  CargarMultiplesArchivosForm
from django.views.generic.detail import DetailView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

class TrabajadorDetailView(DetailView):
    model = Trabajador
    template_name = "expedientes/trabajador_detail.html"
    context_object_name = "trabajador"


class TrabajadorListView(ListView):
    model = Trabajador
    template_name = "expedientes/trabajador_list.html"
    context_object_name = "trabajadores"


class TrabajadorCreateView(CreateView):
    model = Trabajador
    template_name = "expedientes/trabajador_form.html"
    fields = ["nombre", "puesto"]
    success_url = reverse_lazy("lista_trabajadores")


class TrabajadorUpdateView(UpdateView):
    model = Trabajador
    template_name = "expedientes/trabajador_form.html"
    fields = ["nombre", "puesto"]
    success_url = reverse_lazy("lista_trabajadores")


class TrabajadorDeleteView(DeleteView):
    model = Trabajador
    template_name = "expedientes/trabajador_confirm_delete.html"
    success_url = reverse_lazy("lista_trabajadores")


class DocumentoDeleteView(DeleteView):
    model = Documento
    template_name = "expedientes/documento_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("detalle_trabajador", kwargs={"pk": self.object.trabajador.id})
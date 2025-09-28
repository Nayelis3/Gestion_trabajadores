from django import forms
from .models import Documento
import os

class MultipleFileInput(forms.ClearableFileInput):
    #widget para permitir seleccion de varios archivos
    allow_multiple = True

class MultipleFileField(forms.FileField):
    #campo que valida los archivos
    widget = MultipleFileInput

    def clean(self, data, initial=None):
        files = super().clean(data, initial)
        if not isinstance(files, list):
            files = [files]
        for f in files:
            ext = os.path.splitext(f.name)[1].lower()
            if ext not in ['.pdf', '.jpeg', '.jpg', '.png']:
                raise forms.ValidationError(
                    f"Archivo no valido: {f.name}. Solo se permiten imagenes o PDF."
                )
        return files

class CargarMultiplesArchivosForm(forms.Form):
    archivos = MultipleFileField()
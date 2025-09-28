from django.db import models
import os

class Trabajador(models.Model):
    nombre = models.CharField(max_length=100)
    puesto = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.puesto}"

class Documento(models.Model):
    trabajador = models.ForeignKey(
        Trabajador, on_delete=models.CASCADE, related_name="documentos"
    )
    archivo = models.FileField(upload_to="documentos/")

    def __str__(self):
        return f"Documento de {self.trabajador.nombre}: {self.archivo.name}"

    def delete(self, *args, **kwargs):
        # borrar archivo físico si existe
        if self.archivo and os.path.isfile(self.archivo.path):
            os.remove(self.archivo.path)
        super().delete(*args, **kwargs)
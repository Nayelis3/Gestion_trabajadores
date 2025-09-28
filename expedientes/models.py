from django.db import models

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
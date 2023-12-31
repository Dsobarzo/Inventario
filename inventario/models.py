from django.db import models

# Create your models here.

class Inventario(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)

    def __str__(self):
        text = "{0} ({1})"
        return text.format(self.nombre, self.codigo)
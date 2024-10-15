from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    nombre = models.CharField(max_length=30)
    review = models.CharField(max_length=300)
    genero = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to="publicaciones/", blank=True, null=True)

    def __str__(self):
        return self.nombre

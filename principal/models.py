# coding: utf-8

from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Bebida(models.Model):
    nombre = models.CharField(max_length=50)
    ingredientes = models.TextField()
    preparacion = models.TextField()

    def __unicode__(self):
        return self.nombre

class Receta(models.Model):
    # Dato cadena, longitud máxima de 100 y único.
    titulo = models.CharField(max_length=100, unique=True)
    # Dato texto, con texto de ayuda.
    ingredientes = models.TextField(help_text="Redacta los ingredientes")
    # Dato texto, con nombre: Preparación.
    preparacion = models.TextField(verbose_name='Preparación')
    # Dato imagen, se almacenará en la carpeta recetas, titulo: Imágen.
    imagen = models.ImageField(upload_to='recetas', verbose_name='Imagen')
    # Dato Fecha y Hora, almacena la fecha actual.
    tiempo_registro = models.DateTimeField(auto_now=True)
    # Relación al modelo Usuario que Django tiene.
    usuario  = models.ForeignKey(User) # Relación de muchos a uno

    def __unicode__(self):
        return self.titulo

class Comentario(models.Model):
    receta = models.ForeignKey(Receta)
    texto = models.TextField(help_text="Poner un comentario", verbose_name='Comentario')
    def __unicode__(self):
        return self.texto

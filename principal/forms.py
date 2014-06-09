# coding: utf-8
from django.forms import ModelForm
from django import forms
from principal.models import Receta, Comentario

# Formularios a partir de modelos

class RecetaForm(ModelForm):
   # metadato: dato adjunto
    class Meta:
        model = Receta

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario

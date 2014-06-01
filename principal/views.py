# coding: utf-8
from django.shortcuts import render, render_to_response, get_object_or_404
# Importar lo modelos
from principal.models import Comentario, Receta
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import RequestContext

# Crear una vista de ejemplo sobre:

def Sobre(request):
    html = "<html><body><h1>Proyecto de Recetas</h1></body></html>"
    return HttpResponse(html) # Responde un conjuntos de etiquetas de html

def Inicio(request):
    recetas = Receta.objects.all()
    return render_to_response('principal/inicio.html', {'recetas':recetas},
                              context_instance=RequestContext(request))

def Usuarios(request):
    usuarios = User.objects.all()
    recetas = Receta.objects.all()
    titulo = "Página de usuarios y Recetas Registradas"
    return render_to_response('principal/usuarios.html',
                              {'usuarios':usuarios,'recetas':recetas,
                               'titulo':titulo},
                              context_instance=RequestContext(request))

def Recetas(request):
    recetas = Receta.objects.all()
    titulo = "Lista de recetas registradas"
    return render_to_response('principal/lista_recetas.html',
                              {'titulo':titulo, 'recetas':recetas},
                              context_instance=RequestContext(request))

def Detalle_Receta(request, id_receta):
 #   receta = get_object_or_404(Objeto, el dato a buscar en funcion al id)
     dato = get_object_or_404(Receta, pk=id_receta)
     comentarios = Comentario.objects.filter(receta=dato)
     #                        (template, diccionario, context_instance)
     return render_to_response('principal/detalle.html',
                               {'receta': dato, 'comentarios': comentarios})



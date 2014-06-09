# coding: utf-8
from django.shortcuts import render, render_to_response, get_object_or_404
# Importar lo modelos
from principal.models import Comentario, Receta
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from principal.forms import RecetaForm
from django.contrib.auth.forms import UserCreationForm
from principal.forms import ComentarioForm

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

def nueva_receta(request):
    # POST: Es una coleccion de dato que envía
    if request.method == 'POST':
        formulario = RecetaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = RecetaForm()
    return render_to_response('principal/recetaform.html',
                              {'formulario': formulario},
                              context_instance=RequestContext(request))

def nuevo_usuario(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    return render_to_response('principal/nuevousuario.html',
                              {'formulario': formulario},
                              context_instance=RequestContext(request))

def Comentarios(request):
    if request.method == 'POST':
        comenta = ComentarioForm(request.POST)
        if comenta.is_valid():
            comenta.save()
            return HttpResponseRedirect('/')
    else:
        comenta = ComentarioForm()
    return render_to_response('principal/nuevocomentario.html',
                              {'comenta': comenta},
                              context_instance=RequestContext(request))

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recetario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sobre/$', 'principal.views.Sobre'),
    url(r'^$', 'principal.views.Inicio', name="inicio"),
    url(r'^usuarios/$', 'principal.views.Usuarios'),
    url(r'^recetas/$', 'principal.views.Recetas', name="recetas"),
    url(r'^receta/(?P<id_receta>\d+)$', 'principal.views.Detalle_Receta'),
    url(r'^receta/nueva/$', 'principal.views.nueva_receta'),
    url(r'usuario/nuevo/$', 'principal.views.nuevo_usuario'),
    url(r'comenta/$', 'principal.views.Comentarios'),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

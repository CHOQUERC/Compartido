from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'recetario.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT,}),
    url(r'^sobre/$', 'principal.views.Sobre'),
    url(r'^$', 'principal.views.Inicio'),
    url(r'^usuarios/$', 'principal.views.Usuarios'),
    url(r'^recetas/$', 'principal.views.Recetas'),
    url(r'^receta/(?P<id_receta>\d+)$', 'principal.views.Detalle_Receta'),
)

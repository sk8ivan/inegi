from django.conf.urls import patterns, include, url
from .views import Inicio, Exito, AltaUpdate, AltaWindows, Configuracion

urlpatterns = patterns('',
    # Examples:
   	url(r'^$', Inicio.as_view()),
   	#url(r'^$', AltaUpdate , name="inicio"),
   	#url(r'^$', AltaWindows , name="inicio"),
   	url(r'^update/$', AltaUpdate , name="update"),
   	url(r'^windows/$', AltaWindows , name="windows"),
   	url(r'^exito/$', Exito.as_view()),
   	url(r'^configuracion/$', Configuracion.as_view(), name="config")
)

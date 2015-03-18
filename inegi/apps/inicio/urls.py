from django.conf.urls import patterns, include, url
from .views import Inicio

urlpatterns = patterns('',
    # Examples:
   	(r'^$', Inicio.as_view()),
)

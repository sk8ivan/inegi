from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inegi.views.home', name='home'),
    url(r'^', include('apps.inicio.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

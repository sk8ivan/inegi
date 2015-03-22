from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('apps.inicio.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
)

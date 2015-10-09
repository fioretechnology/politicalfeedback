from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('apps.pf.views',
     url(r'^registramozione/$', 'registramozione'),
     url(r'^listamozioni/$', 'listamozioni'),
     url(r'^registramozione/(?P<mozione_id>\d+)/$','registramozione'),
     url(r'^eliminamozione/(?P<id>\d+)/$','eliminamozione'),
)

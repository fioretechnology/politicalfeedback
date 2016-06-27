from django.conf.urls import url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = [
	url(r'^registradocumento/$', views.registradocumento),
	url(r'^listadocumenti/$', views.listadocumenti),
	url(r'^registradocumento/(?P<documento_id>\d+)/$', views.registradocumento ),
	url(r'^eliminadocumento/(?P<id>\d+)/$', views.eliminadocumento ),

	url(r'^registracategoria/$', views.registracategoria),
	url(r'^listacategorie/$', views.listacategorie),
	url(r'^registracategoria/(?P<documento_id>\d+)/$', views.registracategoria ),
	url(r'^eliminacategoria/(?P<id>\d+)/$', views.eliminacategoria ),
]

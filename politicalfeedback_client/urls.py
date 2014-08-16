from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap

from django.conf import settings


urlpatterns = patterns('',

    url(r'^$', 'views.home', name='home'),
    (r'^facebook/', include('django_facebook.urls')),
    (r'^accounts/', include('django_facebook.auth_urls')),

)


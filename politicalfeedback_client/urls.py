from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap

from django.conf import settings


urlpatterns = patterns('',

    url(r'^$', 'views.home', name='home'),
    url(r'logout', 'views.logout', name='logout'),
    url(r'dashboard', 'views.dashboard', name='dashboard'),
    url(r'', include('social_auth.urls')),

)


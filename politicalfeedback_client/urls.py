from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from eplatform.articoli.models import Categoria, Sottocategoria, Articolo

from django.conf import settings

articoli_dict = {
    'queryset': Articolo.objects.filter(attivo = True),
    'date_field': 'data_inserimento',
}

sitemaps = {
    'articoli': GenericSitemap(articoli_dict, priority=0.9),
}


urlpatterns = patterns('',
 
    url(r'', include('eplatform.urls')),

    url(r'^$', 'views.home', name='home'),

    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap',{'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
)



if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
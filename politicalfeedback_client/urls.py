from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

urlpatterns = patterns('',
 
    url(r'^accounts/', include('apps.accounts.urls')),
    url(r'^pf/', include('apps.pf.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'views.home', name='home'),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.conf.urls import  include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

import views

urlpatterns = [
    url(r'^accounts/', include('apps.accounts.urls' )),
    url(r'^pf/', include( 'apps.pf.urls' )),
    url(r'^admin/', admin.site.urls),

    url(r'^gruppo/(?P<id>\d+)/$', views.gruppo ),

    url(r'^$', views.home , name='home'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

	]

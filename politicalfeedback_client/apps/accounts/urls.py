from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.accounts.views',
     url(r'^registra/$', 'registra'),
     url(r'^accedi/$', 'accedi'),
     url(r'^errorelogin/$', 'accedierrore'),
     url(r'^nonattivo/$', 'nonattivo'),
     url(r'^mailesiste/$', 'mailesiste'),
     url(r'^recuperauser/$', 'recuperauser'),
     url(r'^resetpassword/(?P<confirmation_code>.*)/(?P<idutente>.*)/$', 'resetpassword'),
     url(r'^recuperapassword/$', 'recuperapassword'),
     url(r'^cambiapassword/$', 'cambiapassword'),
     url(r'^passwordcambiata/$', 'passwordcambiata'),
     url(r'^errorecambio/$', 'errorecambio'),
     url(r'^inviatoutente/$', 'inviatoutente'),
     url(r'^dati/$', 'dati'),
     url(r'^benvenuto/$', 'benvenuto'),
     url(r'^registrato/$', 'registrato'),
     url(r'^conferma/(?P<confirmation_code>.*)/(?P<idusername>.*)/$', 'conferma'),
     url(r'^nonconfermata/(?P<confirmation_code>.*)/$', 'nonconfermata'),
     url(r'^profile/$', 'profile'),
     url(r'^rimandaattivazione/$', 'rimandaattivazione'),
     url(r'^dashboard/$', 'dashboard'),
     url(r'^attivazione/$', 'attivazione'),
     url(r'^registrasegnalazione/(?P<reply>\d+)/$', 'registrasegnalazione'),
     url(r'^registrasegnalazione/$', 'registrasegnalazione'),
     url(r'^segnalazioneinviata/$', 'segnalazioneinviata'),
     url(r'^listasegnalazioni/$', 'listasegnalazioni'),
)


urlpatterns += patterns('',
     (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)

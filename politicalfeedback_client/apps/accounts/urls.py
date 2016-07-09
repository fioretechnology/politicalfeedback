from django.conf.urls import url

from . import views
from django.contrib.auth.views import logout

urlpatterns = [
	url(r'^registra/$', views.registra),
	url(r'^accedi/$', views.accedi),
	url(r'^errorelogin/$', views.accedierrore),
	url(r'^nonattivo/$', views.nonattivo),
	url(r'^mailesiste/$', views.mailesiste),
	url(r'^recuperauser/$', views.recuperauser),
	url(r'^resetpassword/(?P<confirmation_code>.*)/(?P<idutente>.*)/$', views.resetpassword),
	url(r'^recuperapassword/$', views.recuperapassword),
	url(r'^cambiapassword/$', views.cambiapassword),
	url(r'^passwordcambiata/$', views.passwordcambiata),
	url(r'^errorecambio/$', views.errorecambio),
	url(r'^inviatoutente/$', views.inviatoutente),
	url(r'^dati/$', views.dati),
	url(r'^benvenuto/$', views.benvenuto),
	url(r'^registrato/$', views.registrato),
	url(r'^conferma/(?P<confirmation_code>.*)/(?P<idusername>.*)/$', views.conferma),
	url(r'^nonconfermata/(?P<confirmation_code>.*)/$', views.nonconfermata),
	url(r'^profile/$', views.profile),
	url(r'^rimandaattivazione/$', views.rimandaattivazione),
	url(r'^dashboard/$', views.dashboard),
	url(r'^attivazione/$', views.attivazione),
	url(r'^registrasegnalazione/(?P<reply>\d+)/$', views.registrasegnalazione),
	url(r'^registrasegnalazione/$', views.registrasegnalazione),
	url(r'^segnalazioneinviata/$', views.segnalazioneinviata),
	url(r'^listasegnalazioni/$', views.listasegnalazioni),
	url(r'^elencocitta/(?P<provincia_id>\d+)/$',views.elencocitta),
	url(r'^logout/$', views.logout_view),
	url(r'^member/(?P<id>\d+)/$',views.member),
	url(r'^valuta/(?P<id>\d+)/(?P<valutazione>\d+)/$',views.valuta),

]

from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from apps.accounts.forms import LoginForm
from django.contrib.auth.models import User
from apps.accounts.models import Comune, Profilo
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse


def home(request):

	# domini personalizzati
	current_site = get_current_site(request)
	if current_site.domain == 'www.cinquestellemarcon.org' or current_site.domain == 'cinquestellemarcon.org':
		return HttpResponseRedirect('/gruppo/3857/')

	profili_ids = Profilo.objects.values_list('citta_id')

	comuni = Comune.objects.filter(id__in= profili_ids).distinct()

	return render(request, 'index.html', {'comuni': comuni })

def gruppo(request, id):

	comune = Comune.objects.get(pk = id)

	return render(request, 'gruppo.html', {'comune': comune })

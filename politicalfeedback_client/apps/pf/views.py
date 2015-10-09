from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import Context
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from apps.pf.forms import *
from apps.pf.models import *
import random
import string
from datetime import datetime, timedelta
from django.template.loader import get_template
from django.views.decorators.cache import never_cache
from django.forms.models import inlineformset_factory
from django.shortcuts import get_object_or_404
from django.db import transaction

@login_required
@never_cache
def registramozione(request,mozione_id=None):

	if  mozione_id == None:
		mozione = Mozione()
		mozione.user = request.user
	else:
		mozione = Mozione.objects.get(id = mozione_id)
		
	if request.method == 'POST':
		form = MozioneForm(request.user, request.POST, instance=mozione)


		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/pf/listamozioni')
	else:
		form = MozioneForm(request.user, instance=mozione)


	return render_to_response('pf/registramozione.html',{'form': form, 'id' : mozione_id, 'mozione': mozione}, context_instance=RequestContext(request))

@login_required
@never_cache
def listamozioni(request):
	lista = Mozione.objects.all()
	return render(request, 'pf/listamozioni.html',{'lista': lista,})


@login_required
def eliminamozione(request, id):
	mozione = get_object_or_404(Mozione, pk=id)
	if mozione.user == request.user:
		mozione.delete()
		return HttpResponseRedirect('/pf/listamozioni/')



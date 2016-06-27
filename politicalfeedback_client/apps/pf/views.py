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
def registradocumento(request,documento_id=None):

	if  documento_id == None:
		documento = Documento()
		documento.user = request.user
	else:
		documento = Documento.objects.get(id = documento_id)

	if request.method == 'POST':
		form = DocumentoForm(request.user, request.POST, instance=documento)


		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/pf/lista')
	else:
		form = DocumentoForm(request.user, instance=documento)

	return render(request, 'pf/registradocumento.html', {'form': form, 'id' : documento_id, 'documento': documento})

@login_required
@never_cache
def listadocumenti(request):
	lista = Documento.objects.all()
	return render(request, 'pf/listadocumenti.html',{'lista': lista,})


@login_required
def eliminadocumento(request, id):
	documento = get_object_or_404(Documento, pk=id)
	if documento.user == request.user:
		documento.delete()
		return HttpResponseRedirect('/pf/listadocumenti/')


@login_required
@never_cache
def registracategoria(request,categoria_id=None):

	if  categoria_id == None:
		categoria = Categoria()
		categoria.comune = request.user.profilo.citta
	else:
		categoria = Categoria.objects.get(id = categoria_id)

	if request.method == 'POST':
		form = CategoriaForm(request.user, request.POST, instance=categoria)


		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/pf/listacategorie')
	else:
		form = CategoriaForm(request.user, instance=categoria)

	return render(request, 'pf/registracategoria.html', {'form': form, 'id' : categoria_id, 'categoria': categoria})

@login_required
@never_cache
def listacategorie(request):
	lista = Categoria.objects.all()
	return render(request, 'pf/listacategorie.html',{'lista': lista,})


@login_required
def eliminacategoria(request, id):
	categoria = get_object_or_404(Categoria, pk=id)
	if categoria.comune == request.user.profilo.citta:
		categoria.delete()
		return HttpResponseRedirect('/pf/listacategorie/')

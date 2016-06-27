from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models import Q

from apps.pf.models import *
import datetime


class DocumentoForm(ModelForm):

	def __init__(self, user, *args, **kwargs):
		super(DocumentoForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Documento
		fields = ['data_documento','tipo', 'lettura', 'scrittura','oggetto', 'descrizione']


class CategoriaForm(ModelForm):

	def __init__(self, user, *args, **kwargs):
		super(CategoriaForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Categoria
		fields = ['parent','titolo', 'descrizione', 'globale','provincia', 'gruppo']

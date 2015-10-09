from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db.models import Q

from apps.pf.models import *
import datetime




class MozioneForm(ModelForm):

    def __init__(self, user, *args, **kwargs):
        super(MozioneForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Mozione
        fields = ['oggetto', 'descrizione']


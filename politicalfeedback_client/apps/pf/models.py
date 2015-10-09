from django.db import models

from django.contrib.auth.models import User
from apps.accounts.models import *
from datetime import date, timedelta
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

class Categorie(models.Model):

    comune = models.ForeignKey(Comune)

    parent = models.ForeignKey('self', verbose_name="categoria padre", null=True, blank=True)

    titolo = models.CharField("titolo", max_length=75)
    descrizione = RichTextField(blank=True)

    globale = models.BooleanField(default=False)
    provincia = models.BooleanField(default=False)
    gruppo = models.BooleanField(default=True)


    class Meta:
        ordering = ['titolo', 'pk']
        verbose_name = "Categoria"
        verbose_name_plural = "Categorie"

    def get_absolute_url(self):
        return "/pf/cat/%(cat)s_%(id)d/" % {"cat": slugify(self.titolo), "id": self.id}

    @property
    def is_subcategory(self):
        if self.parent_id:
            return True
        else:
            return False


class Consiglio(models.Model):
    data = models.DateField(auto_now_add=True)
    note = models.TextField()
    youtube_video = models.TextField()

TIPI_DOCUMENTI = (
        ('Mozione', 'Mozione'),
        ('Interpellanza', 'Interpellanza'),
        ('Interrogazione', 'Interrogazione'),
        ('Ordine del Giorno', 'Ordine del giorno'),
        ('Petizione', 'Petizione'),
        ('Proposta di delibera', 'Proposta di delibera'),
        ('Comunicato stampa', 'Comunicato stampa'),
        ('Altro', 'Altro'),
    )

class Documento(models.Model):
    categoria = models.ForeignKey(Categoria)
    utente = models.ForeignKey(User)
    data = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User)
    oggetto = models.TextField()
    descrizione = RichTextField()
    consiglio = models.ForeignKey(Consiglio,blank=True,null=True)
    tipo = models.CharField(max_length=60, choices = TIPI_DOCUMENTI, default = 'Altro')
    pubblica =  models.BooleanField(default=False)

    def __unicode__(self):
        return self.oggetto

    def __str__(self):
        return self.oggetto


class odg(models.Model):
    consiglio = models.ForeignKey(Consiglio)
    descrizione = RichTextField()
    documento = models.OneToOneField(Documento,blank=True,null=True)
    approvata = models.BooleanField(default=False)
    favorevoli = models.IntegerField(blank=True,null=True)
    contrari = models.IntegerField(blank=True,null=True)
    astenuti = models.IntegerField(blank=True,null=True)











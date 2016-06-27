from django.db import models

from django.contrib.auth.models import User
from apps.accounts.models import *
from datetime import date, timedelta
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from reversion import revisions as reversion

class Categoria(models.Model):

    comune = models.ForeignKey(Comune)

    parent = models.ForeignKey('self', verbose_name="categoriapadre", null=True, blank=True)

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

PROTEZIONE = (
        (0, 'Pubblico'),
        (1, 'Pubblico - (Allegati nascosti)'),
        (2, 'Visibile a utenti registrati'),
        (3, 'Visibile a utenti registrati - (Allegati nascosti)'),
        (4, 'Visibile ad attivisti'),
        (5, 'Visibile ad attivisti - (Allegati nascosti)'),
        (6, 'Visibile a consiglieri e collaboratori (gruppo)'),
        (7, 'Visibile a consiglieri e collaboratori (provincia)'),
        (8, 'Visibile a consiglieri e collaboratori (globale)'),
    )


class Documento(models.Model):
    categoria = models.ForeignKey(Categoria)
    comune = models.ForeignKey(Comune)
    autore = models.ForeignKey(User)
    data = models.DateField(auto_now_add=True)
    data_documento = models.DateField()
    oggetto = models.CharField(max_length=240)
    descrizione = RichTextField()
    consiglio = models.ForeignKey(Consiglio,blank=True,null=True)
    tipo = models.CharField(max_length=60, choices = TIPI_DOCUMENTI, default = 'Altro')
    lettura = models.IntegerField(choices = PROTEZIONE, default = 6)
    scrittura = models.IntegerField(choices = PROTEZIONE, default = 6)

    def __unicode__(self):
        return self.oggetto

    def __str__(self):
        return self.oggetto

reversion.register(Documento)




class odg(models.Model):
    consiglio = models.ForeignKey(Consiglio)
    descrizione = RichTextField()
    documento = models.OneToOneField(Documento,blank=True,null=True)
    approvata = models.BooleanField(default=False)
    favorevoli = models.IntegerField(blank=True,null=True)
    contrari = models.IntegerField(blank=True,null=True)
    astenuti = models.IntegerField(blank=True,null=True)

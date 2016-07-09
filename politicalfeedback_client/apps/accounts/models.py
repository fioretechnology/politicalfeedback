from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Provincia(models.Model):
    codice = models.IntegerField()
    provincia = models.TextField()
    sigla = models.CharField(max_length=4,null=True)

    def __unicode__(self):
        return self.provincia

    def __str__(self):
        return self.provincia


class Comune(models.Model):
    provincia = models.ForeignKey(Provincia)
    codice = models.IntegerField(null=True)
    comune = models.TextField()

    def __unicode__(self):
        return self.comune

    def __str__(self):
        return self.comune



TIPO_UTENTE = (
        (0, 'Simpatizzante'),
        (1, 'Attivista'),
        (2, 'Consigliere o incarico amministrativo'),
		(3, 'Cittadino'),
		(4, 'Cittadino - ostile al gruppo'),
    )


class Profilo(models.Model):
    # This field is required.
    user = models.OneToOneField(User)

    # Other fields here
    attiva_accesso_sito = models.BooleanField(default=False)
    confirmation_code = models.CharField(max_length=50,null=True)
    sitoweb = models.CharField(max_length=120,blank=True,null=True)
    telefono = models.CharField(max_length=120)
    cellulare = models.CharField(max_length=120,blank=True,null=True)
    fax = models.CharField(max_length=120,blank=True,null=True)
    tipo_utente = models.IntegerField(choices = TIPO_UTENTE, default = 0)
    avatar = models.ImageField(upload_to = 'loghi/',null=True)

    indirizzo = models.CharField(max_length=220,blank=True,null=True)
    civico = models.CharField(max_length=15,blank=True,null=True)
    cap = models.CharField(max_length=10,blank=True,null=True)
    citta = models.ForeignKey(Comune)
    provincia = models.ForeignKey(Provincia)


    def __unicode__(self):
        return self.user.first_name

    def __str__(self):
        return self.user.first_name

class Valutazione(models.Model):
	user = models.ForeignKey(User)
	valutazione = models.IntegerField(choices = TIPO_UTENTE, default=0)
	votante = models.ForeignKey(User, related_name="votante")




class Segnalazione(models.Model):
    PRIORITA = (
        (u'Urgente', u'Urgente - il problema mi blocca il lavoro'),
        (u'Media', u'Media - Prima possibile'),
        (u'Bassa', u'Bassa - Con calma, quando possibile'),
    )
    TIPO = (
        (u'Errore', u'Errore nel software'),
        (u'Imprecisione', u'Imprecisione nel software'),
        (u'Miglioramento', u'Suggerisci un miglioramento nel software'),
        (u'Nuova funzione', u'Suggerisci una nuova funzione'),
    )
    STATO = (
        (0, u'Chiuso'),
        (1, u'Aperto'),
        (2, u'Sospeso'),
        (3, u'Inserito nella prossima versione'),
        (4, u'Segnato da fare in futuro'),
        (5, u'Posso farlo, ma a pagamento'),
    )
    MODULO = (
        (1, u'Anagrafiche'),
        (2, u'Contabilita'),
        (3, u'Contabilita - Fatture'),
        (4, u'Contabilita - Documenti Di Trasporto'),
        (5, u'Programmazione'),
        (6, u'Pagamenti'),
        (7, u'Programmazione - Schede'),
        (8, u'Email Automatiche'),
        (9, u'Stampe'),
    )
    user = models.ForeignKey(User,blank=True,null=True)
    data_creazione = models.DateField(auto_now_add=True)
    segnalazione = models.ForeignKey("self",blank=True,null=True, related_name='segnalazione_top')
    priorita = models.CharField(max_length=70,blank=True,null=True,choices=PRIORITA)
    tipo = models.CharField(max_length=70,blank=True,null=True,choices=TIPO)
    oggetto = models.CharField(max_length=120)
    messaggio = models.TextField()
    link = models.URLField(blank=True,null=True)
    screenshot = models.ImageField(upload_to="screeshot",blank=True,null=True)
    stato = models.IntegerField(default=1,choices=STATO,blank=True,null=True)
    modulo = models.IntegerField(choices=MODULO,blank=True,null=True)
    faq = models.NullBooleanField(default=False)
    visto = models.BooleanField(default=False)

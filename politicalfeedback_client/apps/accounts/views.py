from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from apps.accounts.forms import *
import random
import string
import datetime
from django.template.loader import get_template
from apps.accounts.models import Profilo, Segnalazione
from django.db import transaction
from django.views.decorators.cache import never_cache
from django.db.models import Q, Sum

@never_cache
def accedi(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    return HttpResponseRedirect('/accounts/dashboard')
                else:
                   return HttpResponseRedirect('/accounts/nonattivo')
            else:
                return HttpResponseRedirect('/accounts/errorelogin')
    
    return render(request, 'accounts/login.html', {'form': form } )

def accedierrore(request):
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form, 'errore' : True } )

@never_cache
def registra(request):
    if request.method == 'POST':
        form = RegistraForm(request.POST, request.FILES)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            #obbligatori
            indirizzo = form.cleaned_data['indirizzo']
            civico = form.cleaned_data['civico']
            citta = form.cleaned_data['citta']
            provincia = form.cleaned_data['provincia']
            cap = form.cleaned_data['cap']
            
            if User.objects.filter(email=email).count() > 0:
                return HttpResponseRedirect('/accounts/mailesiste')
            else:
                user = User.objects.create_user(email, email, password)
                user.first_name = first_name
                user.last_name = last_name
                user.is_active = False
                user.save()
                    
                confirmation_code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(33))
                p = Profilo()
                p.user = user
                p.confirmation_code = confirmation_code
                p.indirizzo = indirizzo
                p.civico = civico
                p.citta = citta
                p.provincia = provincia
                p.partita_iva = partita_iva
                p.cap = cap
                if form.cleaned_data['logo']:
                    p.logo = form.cleaned_data['logo']
                p.save()
                send_registration_confirmation(user)

                return render(request, 'accounts/registrato.html', {'email': user.email})
    else:
        form = RegistraForm()
        
    return render(request, 'accounts/registra.html', {'form': form,})

def rimandaattivazione(request):

    if request.method == 'POST':
        form = RecuperaUtente(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            send_registration_confirmation(user)
            return render(request, 'accounts/attivazioneinviata.html')
    else:
        return render(request, 'accounts/rimandaattivazione.html')

def nonattivo(request):
    form = RecuperaUtente(request.POST)
    return render(request, 'accounts/nonconfermata.html',{'form': form,})


def recuperauser(request):
    if request.method == 'POST':
        form = RecuperaUtente(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            send_username(user)
            return HttpResponseRedirect('/accounts/inviatoutente')
        
    return HttpResponseRedirect('/accounts/login')

def recuperapassword(request):
    if request.method == 'POST':
        form = RecuperaPassword(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.get(email=email)
            confirmation_code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(33))
            p = user.profilo
            p.confirmation_code = confirmation_code
            p.save()   
            send_reset_confirmation(user)
            return HttpResponseRedirect('/accounts/inviatoutente')
        
    return HttpResponseRedirect('/accounts/login')


def resetpassword(request, confirmation_code, idutente):
    try:
        user = User.objects.get(pk=idutente)
        p = user.profilo
        if p.confirmation_code == confirmation_code:
            return render_to_response('accounts/resetpassword.html',{'email': user.email, 'confirmation_code': confirmation_code},context_instance=RequestContext(request))
    except:
        return HttpResponseRedirect('/accounts/nonconfermata/'+ confirmation_code + "/")


def cambiapassword(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = CambiaPassword(request.POST)
            if form.is_valid():
               
                password = form.cleaned_data['password']
                confermapassword = form.cleaned_data['confermapassword']
                if password == confermapassword:
                    request.user.set_password(password)
                    request.user.save()
                    return HttpResponseRedirect('/accounts/passwordcambiata')

    else:
        if request.method == 'POST':
            form = CambiaPasswordReset(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['nuovaPassword']
                confirmpassword = form.cleaned_data['confirmPassword']
                
                confirmation_code = form.cleaned_data['confirmation_code']
                user = User.objects.get(email=email)
                p = user.profilo
                if p.confirmation_code == confirmation_code:
                    if password == confirmpassword:
                        user.set_password(password)
                        user.save()
                        return HttpResponseRedirect('/accounts/passwordcambiata')

    return HttpResponseRedirect('/accounts/errorecambio')

def passwordcambiata(request):
    return render_to_response('accounts/passwordcambiata.html',context_instance=RequestContext(request))

def errorecambio(request):
    return render_to_response('accounts/errorecambio.html',context_instance=RequestContext(request))

def inviatoutente(request):
    return render_to_response('accounts/inviatoutente.html',context_instance=RequestContext(request))

def mailesiste(request):
    return render_to_response('accounts/mailesiste.html',context_instance=RequestContext(request))
        
def registrato(request):
    return render_to_response('accounts/registrato.html',context_instance=RequestContext(request))      

def dati(request):
    if(is_authenticated()):
        if request.method == 'POST':
            form = FirstAccessForm(request.POST)
            if form.is_valid():
                nome = form.cleaned_data['nome']
                cognome = form.cleaned_data['cognome']
                userid = form.cleaned_data['userid']
                email = form.cleaned_data['email']
                password = form.cleaned_data['passwordvalid']
                
                if User.objects.filter(email=email).count() > 0:
                    return HttpResponseRedirect('/accounts/mailesiste')
                else:
                
                    user = User.objects.create_user(userid, email, password)
                    user.first_name = nome
                    user.last_name = cognome
                    user.is_active = False
                    user.save()
                        
                    confirmation_code = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for x in range(33))
                    p = user.profilo
                    p.confirmation_code = confirmation_code
                    p.save()   
                    send_registration_confirmation(user)
                
                    return HttpResponseRedirect('/accounts/benvenuto')
        else:
            form = FirstAccessForm()
        
    return render(request, 'accounts/dati.html', {'form': form,})

def invia_mail(utente, template, to, subject, from_email=''):
    from django.core.mail import EmailMultiAlternatives
    from django.template.loader import get_template
    from django.template import Context
    from email.MIMEImage import MIMEImage
    from django.conf import settings

    d     = Context({ 'nome': utente.first_name, 'cognome': utente.last_name , 'domain': settings.DOMAIN, 'id': utente.id, 'confirmation_code': utente.profilo.confirmation_code })
    plaintext    = get_template('accounts/email/'+template+'.txt')
    htmly        = get_template('accounts/email/'+template+'.html')
    html_content = htmly.render(d)
    text_content = plaintext.render(d)

    if not from_email:
        from_email = settings.EMAIL_CLIENTE

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")

    #logo
    fp = open(settings.STATIC_ROOT + "/img/logo.png", 'rb')
    msg_img = MIMEImage(fp.read())
    fp.close()
    msg_img.add_header('Content-ID', '<{}>'.format("logo.jpg"))
    msg.attach(msg_img)
    
    return msg.send()

    
def send_registration_confirmation(user):
    title   = _("Conferma account")
    invia_mail(user,'send_registration_confirmation',user.email, title, 'no-reply@'+settings.DOMAIN)
    
def send_reset_confirmation(user):
    title   = _("Reimposta la password")
    invia_mail(user,'send_reset_confirmation',user.email, title, 'no-reply@'+settings.DOMAIN)

def send_username(user):
    title = _("Il tuo nome utente")
    invia_mail(user,'send_username',user.email, title, 'no-reply@'+settings.DOMAIN)


def conferma(request, confirmation_code, idusername):
    try:
        user = User.objects.get(id=idusername)
        p = user.profilo
        if p.confirmation_code == confirmation_code:
            user.is_active = True
            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            #login(request,user)
        return HttpResponseRedirect('/accounts/benvenuto/')
    except:
        return HttpResponseRedirect('/accounts/nonconfermata/'+ confirmation_code + "/")

    
def auth_login(request, user):
    login(request, user)

    if len(request.GET['referer'])>0:
        return HttpResponseRedirect(request.GET['referer'])

    
def nonconfermata(request,confirmation_code):
    return render_to_response('accounts/nonconfermata.html',context_instance=RequestContext(request))
    
def benvenuto(request):
    form = LoginForm()
    return render_to_response('accounts/benvenuto.html',{'form' : form },context_instance=RequestContext(request))

def autenticazione(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render_to_response('accounts/index.html',context_instance=RequestContext(request))
        else:
            return render_to_response('accounts/index.html',context_instance=RequestContext(request))
    else:
        return render_to_response('accounts/index.html',context_instance=RequestContext(request))

@login_required
@never_cache
def profile(request):

    formpwd = CambiaPassword()

    mod = False

    if request.method == 'POST':

        formutente = UtenteForm(request.POST, request.FILES)

        if formutente.is_valid():
            user = request.user
            user.first_name = formutente.cleaned_data['first_name']
            user.last_name = formutente.cleaned_data['last_name']
            user.save()
                
            p = request.user.profilo
            p.indirizzo = formutente.cleaned_data['indirizzo']
            p.civico = formutente.cleaned_data['civico']
            p.citta = formutente.cleaned_data['citta']
            p.provincia = formutente.cleaned_data['provincia']
            p.cf = formutente.cleaned_data['cf']
            p.cap = formutente.cleaned_data['cap']
            p.telefono = formutente.cleaned_data['telefono']
            p.fax = formutente.cleaned_data['fax']
            if formutente.cleaned_data['logo']:
                p.logo = formutente.cleaned_data['logo']
            p.save()

            mod = True
    else:
        dati = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'indirizzo': request.user.profilo.indirizzo,
            'civico': request.user.profilo.civico,
            'citta': request.user.profilo.citta,
            'provincia': request.user.profilo.provincia,
            'cf': request.user.profilo.cf,
            'cap': request.user.profilo.cap,
            'telefono': request.user.profilo.telefono,
            'fax': request.user.profilo.fax,


        }
        formutente = UtenteForm(initial=dati)
        

    return render_to_response('accounts/profilo.html',{'formutente' : formutente , 'formpwd': formpwd, 'mod': mod },context_instance=RequestContext(request))

@login_required
@never_cache
def dashboard(request):

    


    return render_to_response('accounts/dashboard.html',
        {
           
        }, context_instance=RequestContext(request))





def attivazione(request):

    if request.user.profilo.scadenza:
        scadenza = request.user.profilo.scadenza
    else:
        scadenza = datetime.datetime.now() + datetime.timedelta(days=365)

    return render(request, 'accounts/attivazione.html',{'scadenza': scadenza})

@login_required
def registrasegnalazione(request,segnalazione_id=None, reply = None):

    if  segnalazione_id == None:
        segnalazione = Segnalazione()
    else:
        segnalazione = Segnalazione.objects.get(utente=request.user, id = segnalazione_id)

    if reply:    
        r = Segnalazione.objects.get(id = reply)
        segnalazione.segnalazione = r
        segnalazione.oggetto = "Re:" + r.oggetto

    if request.method == 'POST':
        form = SegnalazioneForm(request.POST, instance=segnalazione)

        if form.is_valid():
            segnalazione.user = request.user
            segnalazione.priorita = form.cleaned_data['priorita']
            segnalazione.tipo = form.cleaned_data['tipo']
            segnalazione.oggetto = form.cleaned_data['oggetto']
            segnalazione.messaggio = form.cleaned_data['messaggio']
            segnalazione.priorita = form.cleaned_data['priorita']
            segnalazione.link = form.cleaned_data['link']
            segnalazione.screenshot = form.cleaned_data['screenshot']
            segnalazione.priorita = form.cleaned_data['priorita']
            segnalazione.modulo = form.cleaned_data['modulo']
            if reply:
                segnalazione.stato = form.cleaned_data['stato']
                segnalazione.faq = form.cleaned_data['faq']
            else:
                segnalazione.stato = 1
            segnalazione.save()

            return HttpResponseRedirect('/accounts/segnalazioneinviata/')
    else:
        form = SegnalazioneForm(instance=segnalazione)

    return render_to_response('accounts/registrasegnalazione.html',{'form': form,'id' : segnalazione_id}, context_instance=RequestContext(request))

def segnalazioneinviata(request):
    return render_to_response('accounts/segnalazioneinviata.html',context_instance=RequestContext(request))



@login_required
@never_cache
def listasegnalazioni(request):
    if request.user.is_staff:
        lista = Segnalazione.objects.filter(segnalazione = None).order_by('-data_creazione','-id')
    else:
        lista = Segnalazione.objects.filter(segnalazione = None,user = request.user).order_by('-data_creazione')
    return render(request, 'accounts/listasegnalazioni.html',{'lista': lista,})

from django import forms
from django.contrib.auth.models import User
from apps.accounts.models import Comune,Provincia,Profilo,Segnalazione
from django.forms import ModelForm

comuni = Comune.objects.all().order_by('comune')
provincie = Provincia.objects.all().order_by('provincia')

class RegistraForm(forms.Form):   
    
    first_name = forms.CharField(max_length=30, required=True)
    first_name.widget.attrs['pattern'] = '[a-zA-Z]+'
    first_name.widget.attrs['placeholder'] = 'nome'
    last_name = forms.CharField(max_length=30, required=True)
    last_name.widget.attrs['pattern'] = '[a-zA-Z]+'
    last_name.widget.attrs['placeholder'] = 'cognome'
    telefono = forms.CharField(max_length=250, required=True)
    telefono.widget.attrs['placeholder'] = 'telefono'
    telefono.widget.attrs['required'] = 'required'
    email = forms.EmailField(required=True)
    email.widget.attrs['placeholder'] = 'email'
    password = forms.CharField(widget=forms.PasswordInput)
    password.widget.attrs['required'] = 'required'
    indirizzo = forms.CharField(max_length=120,required=True)
    indirizzo.widget.attrs['placeholder'] = 'indirizzo'
    civico = forms.CharField(max_length=120,required=True)
    civico.widget.attrs['placeholder'] = 'numeri civici'
    provincia = forms.ModelChoiceField(provincie,required=True)
    provincia.widget.attrs['required'] = 'required'
    citta = forms.ModelChoiceField(comuni,required=True)
    citta.widget.attrs['required'] = 'required'
    citta.widget.attrs['class'] = 'hide'
    cap = forms.CharField(max_length=120,required=False)
    cap.widget.attrs['placeholder'] = 'CAP'
    cap.widget.attrs['pattern'] = 'integer'
    logo = forms.ImageField(required=False);


    
    def clean_userid(self):
        userid = self.cleaned_data['email']
        try:
            user = User.objects.get(username=userid)
        except User.DoesNotExist:
            return userid
        raise forms.ValidationError(u'%s non disponibile' % userid )


class UtenteForm(forms.Form):
    first_name = forms.CharField(max_length=120,required=True)
    first_name.widget.attrs['required'] = 'required'
    last_name = forms.CharField(max_length=120,required=True)
    last_name.widget.attrs['required'] = 'required'
    telefono = forms.CharField(max_length=250, required=True)
    telefono.widget.attrs['required'] = 'required'
    cellulare = forms.CharField(max_length=250, required=False)
    fax = forms.CharField(max_length=250, required=False)
    cf = forms.CharField(max_length=100, required=True)
    indirizzo = forms.CharField(max_length=120,required=True)
    civico = forms.CharField(max_length=120,required=True)
    provincia = forms.ModelChoiceField(provincie,required=True)
    citta = forms.ModelChoiceField(comuni,required=True)
    cap = forms.CharField(max_length=120,required=False)
    cap.widget.attrs['pattern'] = 'integer'
    logo = forms.ImageField(required=False)


class LoginForm(forms.Form):
    username = forms.EmailField(required=True)
    username.widget.attrs['placeholder'] = 'email'
    username.widget.attrs['required'] = 'required'
    password = forms.CharField(widget=forms.PasswordInput)
    password.widget.attrs['required'] = 'required'
    password.widget.attrs['placeholder'] = 'password'

    
class RecuperaUtente(forms.Form):
    email = forms.EmailField(required=True)
    email.widget.attrs['placeholder'] = 'email'

class RecuperaPassword(forms.Form):
    email = forms.CharField(required=True)
    email.widget.attrs['placeholder'] = 'email'

class CambiaPassword(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    password.widget.attrs['required'] = 'required'
    password.widget.attrs['placeholder'] = 'password'
    confermapassword = forms.CharField(widget=forms.PasswordInput)
    confermapassword.widget.attrs['required'] = 'required'
    confermapassword.widget.attrs['placeholder'] = 'password'
    confermapassword.widget.attrs['data-equalto'] = 'id_password'

class CambiaPasswordReset(forms.Form):
    email = forms.EmailField(required=True)
    nuovaPassword = forms.CharField(widget=forms.PasswordInput)
    confirmPassword = forms.CharField(widget=forms.PasswordInput)
    confirmation_code = forms.CharField(required=True)

class FirstAccessForm(forms.Form):
    email = forms.EmailField(required=True)
    nome = forms.CharField(max_length=5,required=True)
    cognome = forms.CharField(max_length=50,required=True)
    ragione_sociale = forms.CharField(max_length=120,required=True)
    piva = forms.CharField(max_length=50,required=True)
    indirizzo1 = forms.CharField(max_length=120,required=True)
    indirizzo2 = forms.CharField(max_length=120,required=True)
    citta = forms.CharField(max_length=120,required=True)
    regione = forms.CharField(max_length=120,required=True)
    cap = forms.CharField(max_length=120,required=True)
    stato = forms.CharField(max_length=120,required=True)
    
    sitoweb = forms.CharField(max_length=120,required=True)
    tipologia = forms.CharField(max_length=120,required=True)
    
class SegnalazioneForm(ModelForm):

    class Meta:
        model = Segnalazione
        fields = ['priorita','tipo', 'oggetto','messaggio','link','screenshot','modulo','stato','faq','segnalazione']




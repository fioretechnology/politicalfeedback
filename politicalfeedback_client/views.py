from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.utils.translation import ugettext_lazy as _

def home(request):

    return render_to_response('index.html', { } ,context_instance=RequestContext(request))

def dashboard(request):
    return render_to_response('dashboard.html', { } ,context_instance=RequestContext(request))

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')
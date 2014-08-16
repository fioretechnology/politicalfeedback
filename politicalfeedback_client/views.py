from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

def home(request):

    return render_to_response('index.html', { } ,context_instance=RequestContext(request))
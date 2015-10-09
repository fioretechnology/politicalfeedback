from django.shortcuts import render_to_response
from django.template import Context
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from apps.accounts.forms import LoginForm


def home(request):
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
                   return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/accounts/errorelogin')
    

    return render_to_response('index.html',{'form': form }, context_instance=RequestContext(request))

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register/complete')

    else:
        form = UserCreationForm()
    token = {}
    # token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/register.html', token)

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')
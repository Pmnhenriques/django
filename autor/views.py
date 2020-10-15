from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from conta.forms import UserForm
from conta.models import Utilizador
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.core.mail import EmailMessage

# Create your views here.
@csrf_exempt
def registar(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.email = user.username
            user.set_password(user.password)
            user.save()
            registered = True

            return render_to_response('login.html', {'registered': registered}, context)
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render_to_response('registar.html',{'user_form': user_form, 'registered': registered},context)

@csrf_exempt
def login(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                utilizador = Utilizador.objects.filter(user_id=user.id).get()

                request.session['tipo'] = utilizador.tipo

                return HttpResponseRedirect('/ocorrencias/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(email, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('login.html', {'registered':registered}, context)
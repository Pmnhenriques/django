from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from ocorrencias.forms import OcorrenciaForm
from ocorrencias.forms import FiltroForm
from ocorrencias.forms import OcorrenciaForm
from ocorrencias.models import EditarForm
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
        ocorrencia_form = OcorrenciaForm(data=request.POST)
        
        if ocorrencia_form.is_valid():
            ocorrencia = ocorrencia_form.save()
            ocorrencia.dataCriacao = timezone.now()
            ocorrencia.save()
            registered = True

            return render_to_response('geristar.html', {'registered': registered}, context)
        else:
            print(ocorrencia_form.errors)
    else:
        ocorrencia_form = OcorrenciaForm()
    return render_to_response('geristar.html', {'registered': registered}, context)


def editar(request):
    context = RequestContext(request)
    alterado = False

    permissao = request.session['usertype']
    if permissao == 1:
        if request.method == 'POST':
            ocorrencia_form = EditarForm(data=request.POST)
            
            if ocorrencia_form.is_valid() :
                ocorrencia = ocorrencia_form.save()
                ocorrencia.dataActualizacao = timezone.now()
                ocorrencia.autor = request.user
                ocorrencia.save()
                alterado = True

                return render_to_response('editar.html', {'alterado': alterado}, context)
            else:
                print(user_form.errors, profile_form.errors, empresa_form.errors)
        else:
            return render_to_response('editar.html',{ 'alterado': alterado},context)


def ocorrencias(request):
    args = {}
    args.update(csrf(request))
    permissao = request.session['usertype']
    if permissao == 1 or permissao == 2:

        if request.method == 'POST':

            ocorrencias = Ocorrencias.objects.filter(autor = request.POST['autor'], categoria = request.POST['categoria'], localizacao = request.POST['localizacao'])

            return render_to_response('ocorrencias.html', {'ocorrencias':ocorrencias})

        else:
            return render_to_response('ocorrencias.html', args)
    else:
        raise PermissionDenied()
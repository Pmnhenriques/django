from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from ocorrencias.models import OcorrenciaForm
from django.forms.extras.widgets import SelectDateWidget

class OcorrenciaForm(forms.ModelForm):
   categorias = (('1', 'CONSTRUCTION'), ('2', 'SPECIAL_EVENT'), ('3', 'INCIDENT'), ('4', 'WEATHER_CONDITION'), ('5', 'ROAD_CONDITION'))
   categoria = forms.ChoiceField(widget=forms.Select, choices=categorias, required=True)
   descricao = forms.CharField(label=(u'descricao'),widget=forms.TextInput(attrs={'placeholder': 'Descrição'}))
   localizacao = forms.CharField(label=(u'localizacao'),widget=forms.TextInput(attrs={'placeholder': 'Localização'}))
   
   class Meta:
      model = Ocorrencia
      fields = ('categorias', 'descricao', 'localizacao')


class FiltroForm(forms.ModelForm):
   categorias = (('1', 'CONSTRUCTION'), ('2', 'SPECIAL_EVENT'), ('3', 'INCIDENT'), ('4', 'WEATHER_CONDITION'), ('5', 'ROAD_CONDITION'))
   categoria = forms.ChoiceField(widget=forms.Select, choices=categorias, required=True)
   autor = forms.CharField(label=(u'autor'),widget=forms.TextInput(attrs={'autor': 'Autor'}))
   localizacao = forms.CharField(label=(u'localizacao'),widget=forms.TextInput(attrs={'placeholder': 'Localização'}))
   
   class Meta:
      model = Ocorrencia
      fields = ('categoria', 'autor', 'localizacao')


class EditarForm(forms.ModelForm):
   estados = (('1', 'por validar'), ('2', 'validdo'), ('3', 'resolvido'))
   estado = forms.ChoiceField(widget=forms.Select, choices=estados, required=True) 
   
   class Meta:
      model = Ocorrencia
      fields = ('estado')
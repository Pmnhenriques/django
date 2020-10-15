from django import forms
from django.contrib.auth.models import User
from autor.models import autor

from django.utils.translation import ugettext as _

class UserForm(forms.ModelForm):
   password = forms.CharField(widget=forms.PasswordInput())
   password2 = forms.CharField(widget=forms.PasswordInput, label=_("Password (again)"))
   username = forms.EmailField(label=(u'Email Address'))
   tipos = (('1', 'Administrador'), ('2', 'utilizador'))
   tipo = forms.ChoiceField(widget=forms.Select, choices=tipos, required=True)


    class Meta:
        model = User
        fields = ('username', 'password',)

    def clean(self):
        if 'password' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("As Palavra-Chave não coincidem."))
        return self.cleaned_data

    def clean_username(self):
        """
        Validate that the username is alphanumeric and is not already in use.
        """
        existing = User.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("O email já se encontra registado."))
        else:
            return self.cleaned_data['username']

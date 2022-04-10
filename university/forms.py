from django import forms
from .models import Registration
from django_countries.widgets import CountrySelectWidget



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {'gsp_location': CountrySelectWidget()}
        labels = {
            'name':'Full Names',
            'height':'Height (feet)',
            'gsp_location':'Location'
        }

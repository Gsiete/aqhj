from dal import autocomplete

from django import forms

from main.models import Stadium


class StadiumForm(forms.ModelForm):
    class Meta:
        model = Stadium
        fields = ('__all__')
        widgets = {
            'city': autocomplete.ModelSelect2(url='city-autocomplete')
        }

from django import forms
from .models import ClimateData

class ClimateDataForm(forms.Form):
    year = forms.ChoiceField(
        choices=[(year, year) for year in ClimateData.objects.values_list('year', flat=True).distinct()],
        label='Year',
        required=True
    )
    season = forms.ChoiceField(
        choices=[(season, season) for season in ClimateData.objects.values_list('season', flat=True).distinct()],
        label='Season',
        required=True
    )

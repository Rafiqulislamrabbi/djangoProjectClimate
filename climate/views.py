# climate/views.py
from django.shortcuts import render
from .models import ClimateData
from .forms import ClimateDataForm


def query_climate_data(request):
    form = ClimateDataForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ClimateDataForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            season = form.cleaned_data['season']
            try:
                climate_data = ClimateData.objects.get(year=year, season=season)
                context.update({
                    'climate_data': climate_data,
                    'year': year,
                    'season': season,
                })
            except ClimateData.DoesNotExist:
                context['error'] = "No data found for the specified year and season."

    return render(request, 'query_climate_data.html', context)

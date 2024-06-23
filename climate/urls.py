from django.urls import path
from climate import views

app_name = 'climate'

urlpatterns=[
    path('', views.query_climate_data, name='query_climate_data'),

]

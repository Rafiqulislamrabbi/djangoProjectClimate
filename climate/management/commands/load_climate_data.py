import json
from django.core.management.base import BaseCommand
from climate.models import ClimateData

class Command(BaseCommand):
    help = 'Load climate data from JSON file'

    def handle(self, *args, **kwargs):
        # Define the path to the JSON file
        json_file_path = 'Model-Predicted-Data.json'

        # Open and read the JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)

        # Parse the JSON data and save it to the model
        for item in data["Sheet1"]:
            ClimateData.objects.create(
                year = item["Year"],
                season = item["Season"],
                rainfall_mm = item["Rainfall (mm)"],
                rainfall_change_percentage = item["% Change of Rainfall with respect to 2024"],
                temperature_celsius = item["Temperature (Degree Celcius)"],
                temperature_change_celsius = item["Change of Temperature (Degree Celcius) with respect to 2024"]
            )

        self.stdout.write(self.style.SUCCESS('Successfully loaded climate data'))

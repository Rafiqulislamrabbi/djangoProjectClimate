
from django.db import models
class ClimateData(models.Model):
    year = models.IntegerField()
    season = models.CharField(max_length=20)
    rainfall_mm = models.FloatField()
    rainfall_change_percentage = models.FloatField()
    temperature_celsius = models.FloatField()
    temperature_change_celsius = models.FloatField()

    def __str__(self):
        return f"{self.year} - {self.season}---{self.rainfall_mm} --- {self.rainfall_change_percentage}--{self.temperature_change_celsius}---{self.temperature_celsius}"

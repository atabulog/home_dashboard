from django.db import models

# Create your models here.
class Local_weather(models.Model):
    timestamp = models.DateTimeField("recorded timestamp")
    temp_C = models.FloatField("temperature C", default=None)
    rel_humidity = models.FloatField("relative humidity", default=None)
    precipitation = models.FloatField("precipitation", default=None)


    def __str__(self) -> str:
        return f"\nTime: {self.timestamp}\nTemp: {self.temp_C} [C]\nhumidity: {self.rel_humidity}%\nprecip: {self.precipitation}%\n"
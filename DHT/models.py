from django.db import models


class Dht11(models.Model):
    temperature = models.FloatField(null=True)
    humidity = models.FloatField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f"{self.temperature} °C / {self.humidity} %"
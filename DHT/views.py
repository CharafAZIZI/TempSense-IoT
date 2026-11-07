import math
from django.shortcuts import render
from .models import Dht11


def dashboard(request):
    # Récupérer les 10 dernières mesures
    mesures = Dht11.objects.order_by('-date')[:10]

    # Récupérer la dernière mesure
    derniere_mesure = mesures.first()

    # Vérifier que les valeurs sont numériques et valides
    temperature = None
    humidity = None

    if derniere_mesure:
        try:
            temp = float(derniere_mesure.temperature)
            hum = float(derniere_mesure.humidity)

            if math.isfinite(temp):
                temperature = temp

            if math.isfinite(hum):
                humidity = hum

        except (TypeError, ValueError):
            pass

    context = {
        'temperature': temperature,
        'humidity': humidity,
        'mesures': mesures,
        'derniere_mesure': derniere_mesure,
    }

    return render(request, 'DHT/dashboard.html', context)

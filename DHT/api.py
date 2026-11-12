import logging
import telebot

from .models import Dht11
from .serializers import DHT11serialize
from rest_framework.decorators import api_view
from rest_framework import status, generics
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)


@api_view(['GET'])
def Dlist(request):
    all_data = Dht11.objects.all()
    data = DHT11serialize(all_data, many=True).data
    return Response({'data': data})


class Dhtviews(generics.CreateAPIView):
    queryset = Dht11.objects.all()
    serializer_class = DHT11serialize

    def perform_create(self, serializer):
        # Enregistrer la mesure
        data = serializer.save()

        # Vérifier si la température dépasse 25°C
        if data.temperature > 25:

            # Notification par Gmail
            try:
                send_mail(
                    subject="Alerte TempSense IoT",
                    message=f"Attention ! Température élevée : {data.temperature} °C",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )
            except Exception:
                logger.exception("Erreur lors de l'envoi de l'email")

            # Notification par Telegram
            try:
                bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)
                bot.send_message(
                    settings.TELEGRAM_CHAT_ID,
                    f"⚠️ Alerte TempSense IoT ! Température élevée : {data.temperature} °C"
                )
            except Exception:
                logger.exception("Erreur lors de l'envoi du message Telegram")
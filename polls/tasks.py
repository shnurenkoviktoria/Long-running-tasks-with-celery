from .models import Number
import os
from twilio.rest import Client

from celery import shared_task

TWILIO_ACCOUNT_SID = 'ACec2a35c8a53e4f514808e3bfb75bb0b7'
TWILIO_TOKEN= '3f464827d4cddfd36e95f0235b12972f'
TWILIO_NUMBER="+12707166231"
try:
    client=Client(TWILIO_ACCOUNT_SID, TWILIO_TOKEN)
except Exception as e:
    print(f"An error occurred: {str(e)}")


@shared_task
def send_messages(number):
    # number = Number.objects.last("number")
    message = client.messages.create(from_=TWILIO_NUMBER, to=number)

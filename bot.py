from linebot.client import LineBotClient
from django.http import HttpResponse

import os

credentials = {
    'channel_id': str(os.environ.get('Channel_ID', 0)),
    'channel_secret': str(os.environ.get('Channel_Secret', 0)),
    'channel_mid': str(os.environ.get('MID', 0)),
}

client = LineBotClient(**credentials)

def messageHandler(request):
    return HttpResponse('Hello!')
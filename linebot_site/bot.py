from linebot.client import LineBotClient
from django.http import HttpResponse

import os

credentials = {
    'channel_id': str(os.environ.get('Channel_ID')),
    'channel_secret': str(os.environ.get('Channel_Secret')),
    'channel_mid': str(os.environ.get('MID')),
}

client = LineBotClient(**credentials)

def messageHandler(request):
    return HttpResponse(request.get_data())
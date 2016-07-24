from linebot.client import LineBotClient
from linebot.receives import Receive
from django.http import HttpResponse

import os

credentials = {
    'channel_id': str(os.environ.get('Channel_ID', 0)),
    'channel_secret': str(os.environ.get('Channel_Secret', 0)),
    'channel_mid': str(os.environ.get('MID', 0)),
}

client = LineBotClient(**credentials)

def messageHandler(request):
    
    # check http request method
    if request.method == 'GET':
        return HttpResponse()
    elif request.method == 'POST':
        pass
    
    # get the sender's mid and message
    receive = Receive(request.body)
    midSender = receive[0].to_mid
    msgSender = receive[0].message
    
    # construct the reply
    reply = msgSender
    
    # send the reply
    client.send_text(midSender, reply)
    
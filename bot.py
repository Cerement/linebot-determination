from linebot.client import LineBotClient
from linebot.receives import Receive
from linebot import messages
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
    
    # for each message
    receive = Receive(request.body)
    for message in receive:
        
        # get sender's mid
        midSender = message['from_mid']
        
        # for text messages
        if isinstance(message['content'], messages.TextMessage):
            
            # get the sender's mid and message
            msgSender = message['content']['text']
            
            # construct the reply
            reply = msgSender
            
            # send the reply
            client.send_text(to_mid = midSender, text = reply)
            
    return HttpResponse()
            
    
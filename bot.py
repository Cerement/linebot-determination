# -*- coding: utf-8 -*-

from linebot.client import LineBotClient
from linebot.receives import Receive
from linebot import messages
from django.http import HttpResponse

import os, re

credentials = {
    'channel_id': str(os.environ.get('Channel_ID', 0)),
    'channel_secret': str(os.environ.get('Channel_Secret', 0)),
    'channel_mid': str(os.environ.get('MID', 0)),
}

client = LineBotClient(**credentials)

# support functions
def getRandomBooleen():
    pass

def getRandomPrefix():
    pass

def getRandomPostfix():
    pass

def getRandomEmoji():
    pass

def getRandomHint(): # for cases not recognized
    pass

# /callback/
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
            msgSender = message['content']['text'].encode('utf-8')
            
            # analyze the message and construct the reply
            reply = ''
            matchObjABA = re.search(ur'([\u2E80-\u9FFF])不\1', msgSender) # 好不好 
            if matchObjABA: # 好不好
                ch = matchObjABA.group(1) # 好
                reply = ch
            
            else: # not a true/false question
                reply = u'我不太懂你的意思'
            
            # send the reply
            client.send_text(to_mid = midSender, text = reply)
            
    return HttpResponse()
            
    
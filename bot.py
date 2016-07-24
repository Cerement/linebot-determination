# -*- coding: utf-8 -*-

from linebot.client import LineBotClient
from linebot.receives import Receive
from linebot import messages
from django.http import HttpResponse
from predefinedtexts import PredefinedTexts

import os, re, numpy

credentials = {
    'channel_id': str(os.environ.get('Channel_ID', 0)),
    'channel_secret': str(os.environ.get('Channel_Secret', 0)),
    'channel_mid': str(os.environ.get('MID', 0)),
}

client = LineBotClient(**credentials)

# support functions
def getHelpMsg():
    
    return PredefinedTexts.helpMsg

def getRandomAnswer():
    "Return 1 (true), -1 (false) or 0 (don't know)"
    
    return numpy.random.choice([1, -1, 0], p=[0.45, 0.45, 0.1])

def getRandomPrefix():
    
    return numpy.random.choice(PredefinedTexts.prefixes)

def getRandomPostfix():
    
    return numpy.random.choice(PredefinedTexts.postfixes)

def getRandomNoAnswer():
    
    return numpy.random.choice(PredefinedTexts.noAnswers)

def getRandomEmoji():
    
    return numpy.random.choice(PredefinedTexts.emojis)

def getRandomHint(): # for cases not recognized
    
    return numpy.random.choice(PredefinedTexts.hintMsgs)

def getRandomCryMsg(): # QQ
    
    return numpy.random.choice(PredefinedTexts.cryMsgs)

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
            msgSender = message['content']['text']
            
            # analyze the message and construct the reply
            reply = ''
            matchObjHelp = re.search(ur'^你是誰$', msgSender) # help
            matchObjCry = re.search(r'^QQ$', msgSender) # QQ
            matchObjABA = re.search(ur'([\u2E80-\u9FFF])不\1', msgSender) # 好不好 
            
            if matchObjHelp: # help
                reply = getHelpMsg()
                
            elif matchObjCry: # QQ
                reply = getRandomCryMsg()
            
            elif matchObjABA: # 好不好
                ch = matchObjABA.group(1) # 好
                
                # generate random answer
                ans = getRandomAnswer()
                if ans == 1: # yes
                    reply = getRandomPrefix() + ch + getRandomPostfix()
                    
                elif ans == -1: # no
                    reply = getRandomPrefix() + u'不' + ch + getRandomPostfix()
                    
                elif ans == 0: # no answer
                    reply = getRandomNoAnswer()
                    
                reply += ' ' + getRandomEmoji()
            
            else: # not a true/false question
                reply = getRandomHint() + ' ' + getRandomEmoji()
            
            # send the reply
            client.send_text(to_mid = midSender, text = reply)
            
    return HttpResponse()
            
    
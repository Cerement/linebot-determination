from linebot.client import LineBotClient

import os

credentials = {
    'channel_id': str(os.environ.get('Channel_ID')),
    'channel_secret': str(os.environ.get('Channel_Secret')),
    'channel_mid': str(os.environ.get('MID')),
}

client = LineBotClient(**credentials)


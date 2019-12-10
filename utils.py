import os

from linebot import LineBotApi, WebhookParser
from linebot.models import *


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_url(user_id, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(origional_content_url=img_url, preview_image_url=img_url)
    line_bot_api.push_message(user_id, message)
    
    return "sent image"

    


"""
def send_button_message(id, text, buttons):
    pass
"""

import os

from linebot import LineBotApi, WebhookParser
from linebot.models import *


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_image_url(reply_token, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(original_content_url=img_url, preview_image_url=img_url)
    line_bot_api.push_message("U46b5bdcccc8124e05d79148943af39e5", message)
    
    return "sent image"

def send_sticker(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = StickerSendMessage(package_id='11537',sticker_id='52002759')
    line_bot_api.push_message("U46b5bdcccc8124e05d79148943af39e5", message)
    
    return "sent sticker"

def send_gif(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = VideoSendMessage(original_content_url='https://gcs-vimeo.akamaized.net/exp=1576034848~acl=%2A%2F871187021.mp4%2A~hmac=c2f1aa7bae26712b28a16f3e66ddc45a3de02f6e814351dfef8098bce4ccc8ed/vimeo-prod-skyfire-std-us/01/3507/9/242538649/871187021.mp4',preview_image_url='https://ak7.picdn.net/shutterstock/videos/1023393757/thumb/2.jpg')
    line_bot_api.push_message("U46b5bdcccc8124e05d79148943af39e5", message)
    
    return "sent video"

def push_message(user_id, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.push_message("U46b5bdcccc8124e05d79148943af39e5",TextSendMessage(text=text))

    return "ok"
    

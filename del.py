import telebot
import requests
from PIL import Image, ImageDraw, ImageFont
from telebot import types
# import logging

# logger = telebot.logger
# telebot.logger.setLevel(logging.DEBUG)

# bot = telebot.TeleBot("1922857274:AAGoFyM2kXlcpsPbdrmhz1pTwZCKjeMlRIw", parse_mode=None)
# url = "https://api.telegram.org/bot1922857274:AAGoFyM2kXlcpsPbdrmhz1pTwZCKjeMlRIw/"

image = Image.open("random.jpg")
title_font = ImageFont.truetype('Zen_loop/ZenLoop-Regular.ttf', 200)
title_text = "The Beauty of Nature"
image_edit = ImageDraw.Draw(image)
image_edit.text((15,15), title_text, (237, 230, 211), font=title_font)
image.save("result.jpg")

# text="Hello"    
# img="https://unsplash.com/photos/4Y-Rdj1e1es" 
# bot.send_message(497252050,'https://api.telegram.org/bot1922857274:AAGoFyM2kXlcpsPbdrmhz1pTwZCKjeMlRIw/sendMessage?chat_id=497252050&parse_mode=markdown&text='+"[​​​​​​​​​​​]("+img+")"+text)

# text="Hello"    
# img="https://unsplash.com/photos/4Y-Rdj1e1es" 
# bot.send_message(497252050,f'{text}\n{img}')

# bot.polling()

# "https://api.telegram.org/bot1922857274:AAGoFyM2kXlcpsPbdrmhz1pTwZCKjeMlRIw/deleteWebhook"

# files = {'photo': open("C:\\User/random.jpg", 'rb')}
# resp = requests.post('https://api.telegram.org/bot1922857274:AAGoFyM2kXlcpsPbdrmhz1pTwZCKjeMlRIw/sendPhoto?chat_id=-497252050&caption=just_photo', files=files)
# print(resp.status_code)

# bot.polling()



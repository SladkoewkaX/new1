import telebot
import requests
from PIL import Image, ImageDraw, ImageFont
from telebot import types

bot = telebot.TeleBot("1922857274:AAGoFyM2kXlcpsPbdrmhz1pTwZCKjeMlRIw", parse_mode=None)



@bot.message_handler(content_types=['text'])
def answer_bot(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Здравствуйте.")
    elif message.text == "Пока":
        bot.send_message(message.from_user.id, "Увидимся.")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Варианта выбора: Привет, Пока, Стикер 1, Стикер 2, Стикер 3, Фото, Фото 2.")
    elif message.text == "Стикер 1":
        bot.send_sticker(message.chat.id, 'https://chpic.su/_data/stickers/h/hamster_senia/hamster_senia_003.webp' )
    elif message.text == "Стикер 2":
        bot.send_sticker(message.chat.id, 'https://chpic.su/_data/stickers/h/hamster_senia/hamster_senia_001.webp' )
    elif message.text == "Стикер 3":
        bot.send_sticker(message.chat.id, 'https://chpic.su/_data/stickers/h/hamster_senia/hamster_senia_033.webp' )
    elif message.text == 'Фото':
        bot.send_photo(message.chat.id, 'https://memepedia.ru/wp-content/uploads/2019/01/screenshot_6-5-360x270.png')
    elif message.text == 'Фото 2':
        bot.send_photo(message.chat.id, 'https://cs11.pikabu.ru/post_img/big/2020/02/25/0/1582580593168654510.jpg')
    else:
        bot.send_message(message.from_user.id, "Прости, но я не знаю такую команду.Если хочешь узнать какие команды я знаю, то напиши /help.")

markup = types.ReplyKeyboardMarkup()
btn1 = types.KeyboardButton('Привет')
btn2 = types.KeyboardButton('Пока')
btn3 = types.KeyboardButton('Стикер 1')
btn4 = types.KeyboardButton('Стикер 2')
btn5 = types.KeyboardButton('Стикер 3')
btn6 = types.KeyboardButton('Фото')
btn7 = types.KeyboardButton('Фото 2')
markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
bot.send_message(497252050, "Выберите по желанию ", reply_markup=markup)


bot.polling()
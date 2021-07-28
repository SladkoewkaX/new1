# import telebot
# import os
# from flask import Flask, request

# token = "1865643613:AAFzY1Um1kL-KbhjYDUg-0i-FxOTZh54dMo"
# # https://api.telegram.org/bot1865643613:AAFzY1Um1kL-KbhjYDUg-0i-FxOTZh54dMo/setWebhook?url=https://6a50b0e96f7c.ngrok.io

# server = Flask(__name__)
# bot = telebot.TeleBot(token, parse_mode=None)

# @server.route("/", methods=["POST"])
# def receive_update():
#  bot.process_new_updates(
#   [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
#  )
#  return {'ok':True}

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
#  bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#  bot.reply_to(message, message.text)

# @bot.message_handler(content_types=['photo'])
# def photo(message):
#  bot.send_photo(message.chat_id, message.photo)

# @server.route("/" + token, methods=["POST"])
# def getMessage():
#  bot.process_new_updates(
#   [
#    telebot.types.Update.de_json(
#     request.stream.read().decode("utf-8")
#    )
#   ]
#  )
#  return "!", 200

# if __name__ == "__main__":
#     server.run()
import os 
from Image import image_to_bw
import telebot
import uuid
from PIL import Image

token = "1922857274:AAGoFyM2kXlcpsPbdrmhz1pTwZCKjeMlRIw"

bot = telebot.TeleBot(token, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
 bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
 bot.reply_to(message, message.text)

@bot.message_handler(content_types=['photo'])
def photo(message):
    save_url = "/Users/User/new1/image/"
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    image_name = str(uuid.uuid4())+ '.jpg'
    downloaded_file = bot.download_file(file_info.file_path)
    with open(save_url+image_name, 'wb') as new_file:
        new_file.write(downloaded_file)
    path_to_bw = image_to_bw(save_url+image_name)
    with Image.open(path_to_bw) as img:
        bot.send_photo(message.chat.id, img)
    os.remove(path_to_bw)

bot.polling()
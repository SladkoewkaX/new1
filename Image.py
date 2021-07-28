from PIL import Image, ImageDraw, ImageFont
import numpy as np
from PIL import Image
import os
import telebot

path = "/Users/User/new1/image/second.jpg"

def image_to_bw(path_to_image):
    path_to_save = "/Users/User/new1/result_im"
    image_name = path_to_image.split('/')[-1]
    img = Image.open(path_to_image)
    arr = np.asarray(img, dtype='uint8')
    x, y, _ = arr.shape
    k = np.array([[[0.2989, 0.587, 0.114]]])
    arr2 = np.round(np.sum(arr*k, axis=2)).astype(np.uint8).reshape((x, y))
    img2 = Image.fromarray(arr2)
    img2.save(path_to_save+image_name)
    os.remove(path_to_image)
    return path_to_save+image_name

# bot.polling()
# image_to_bw(path)





    # image_name = str(uuid.uuid4())+ '.jpg'
    # downloaded_file = bot.download_file(file_info.file_path)
    # with open(image_name, 'wb') as new_file:
    #     new_file.write(downloaded_file)

    # url = "https://api.telegram.org/bot1731475338:AAFju7bvSaIDTf5eMG6CVsS4cSA4Aqwasis/"


# response = requests.get(url+'getUpdates')
# for i in response.json()['result']:
#     print(i)

# bot.polling()


# url2 = 'https://api.telegram.org/bot1731475338:AAFju7bvSaIDTf5eMG6CVsS4cSA4Aqwasis/sendMessage?chat_id=497252050&text=Привет,я тестирую'

# for i in range(4):
#      response = requests.get(url2)
#      print(response)

# @bot.message_handler(content_types=['photo'])
# def echo_all(message):
#     bot.reply_to(message, message.text)




# path = "/Users/User/new1/image/random.jpg"

# def color(place):
#     path_to_save = "/Users/User/new1/result_im2/"
#     image_name = place.split('/')[-1]
#     image = Image.open(place)
#     title_font = ImageFont.truetype('Zen_loop/ZenLoop-Regular.ttf', 200)
#     title_text = "The Beauty of Nature"
#     image_edit = ImageDraw.Draw(image)
#     image_edit.text((15,15), title_text, (237, 230, 211), font=title_font)
#     image.save(path_to_save+image_name)

# color(path)
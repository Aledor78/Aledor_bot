import telebot
import random
from telebot import apihelper
from telebot.types import Message
TOKEN = '420586712:AAFK5G3ZTKzG_pHZKywfhj3yQjtR3DpeTC8'

bot = telebot.TeleBot(TOKEN)

'''
apihelper.proxy = {
    #'http': 'socks5://tg.gvg.pw:5678',
    'https': 'socks5://127.0.0.1:9050',
}
'''

@bot.message_handler(content_types=['text'])
def start(message: Message):

    bot.reply_to(message, str(random.random()))


bot.polling()

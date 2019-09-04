import telebot
import random
from telebot import apihelper
from telebot.types import Message
from telebot import types
TOKEN = '420586712:AAFK5G3ZTKzG_pHZKywfhj3yQjtR3DpeTC8'

bot = telebot.TeleBot(TOKEN)

'''
apihelper.proxy = {
    #'http': 'socks5://tg.gvg.pw:5678',
    'https': 'socks5://127.0.0.1:9050',
}
'''

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_manual=types.KeyboardButton("Manual")
markup_menu.add(btn_manual)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Добро рожаловать! Сперва прочитайте инструкцию.', reply_markup=markup_menu)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Manual":
        bot.reply_to(message, '1...2...3...', reply_markup=markup_menu)
    else:
        bot.reply_to(message, str(random.random()), reply_markup=markup_menu)

'''
@bot.message_handler(content_types=['text'])
def start(message: Message):

    bot.reply_to(message, str(random.random()))
'''

bot.polling()

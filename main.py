import telebot
from telebot import types
from telebot.types import WebAppInfo


from settings import SETTINGS

bot = telebot.TeleBot(SETTINGS['TG']['TOKEN'], parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(True)
    markup.add(types.KeyboardButton('Каталог', web_app=WebAppInfo(url='https://aiogram.dev/')))

    bot.send_message(message.chat.id,
                     'Привет, выбирай кроссовки в нашем магазине.', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,
                     "По всем вопоросам обращайтесь @Ioann_business")
























bot.infinity_polling()
import urllib.request
from http.client import HTTPResponse
from telebot import types
import telebot
resp: HTTPResponse = urllib.request.urlopen("https://google.ru")

#сам бот
bot = telebot.TeleBot('6266288635:AAHFkuMgS-WDrn_rt9sEKmAdZhyy_9DjZrs')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Добрый день!!! <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id, f'Добрый день! <b>{message.from_user.first_name}</b>', parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f'Твой id: {message.from_user.id}', parse_mode='html')
    elif message.text == "photo":
        photo = open('games.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю!')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Крутое фото!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://edu.tinkoff.ru"))
    bot.send_message(message.chat.id, 'Перейдите на сайт!', reply_markup=markup)


bot.polling(none_stop=True)
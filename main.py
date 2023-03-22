import telebot
import json
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot('6215252216:AAGgcdkwjwM0oWlJvzAYmoEKXt0N2oaOwSY')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я телеграм бот для парсинга текста с сайта. Введите команду /parse для начала работы.')

@bot.message_handler(commands=['parse'])
def parse_website(message):
    url = 'http://35.234.109.231/api/post/'
    response = requests.get(url)
    data = json.loads(response.text)
    owner, descr = '', ''
    for i in data:
        for k, v in i.items():
            if k == 'owner':
                owner = v

            elif k == 'descriptions':
                descr = v

            if owner and descr:
                bot.send_message(message.chat.id, f'Пост пользователя: {owner}\n{descr}')
                owner, descr = '', ''

bot.polling()
import telebot
import json
import requests
from bs4 import BeautifulSoup
from io import BytesIO

bot = telebot.TeleBot('6215252216:AAGgcdkwjwM0oWlJvzAYmoEKXt0N2oaOwSY')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я телеграм бот для парсинга текста с сайта. Введите команду /parse для начала работы.')

@bot.message_handler(commands=['parse'])
def parse_website(message):
    url = 'http://35.234.109.231/api/post/'
    response = requests.get(url)
    data = json.loads(response.text)
    owner, descr, med = '', '', ''
    for i in data:
        for k, v in i.items():
            if k == 'owner':
                owner = v

            elif k == 'descriptions':
                descr = v
            
            elif k == 'media':
                for j in v:
                    for k2, v2 in j.items():
                        if k2 == 'media':
                            med = v2

            if owner and descr and med:
                response = requests.get(med)
                photo = BytesIO(response.content)
                bot.send_photo(message.chat.id, photo,caption=f'Пост пользователя: {owner}\n{descr}')
                owner, descr, med = '', '', ''

            elif owner and descr:
                bot.send_message(message.chat.id, f'Пост пользователя: {owner}\n{descr}')
                owner, descr, med = '', '', ''

bot.polling()
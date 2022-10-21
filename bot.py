import os

import telebot
from dotenv import load_dotenv

import main


load_dotenv()
telegram_token = os.environ['TG_TOKEN']
bot = telebot.TeleBot(token=telegram_token)
HELP = '''
/start - помощь
/qrcode <ссылка> - получить qrcode
/git - получить ссылку на проект
'''
STRAT = 'Привет! Это бот для создания QR кодов. Нужго ввести команду /qrcode и далее, через пробел указать ссылку. Ниже представлены доступны команды:'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, STRAT)
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=['qrcode'])
def qrcode(message):
    text = message.text
    if text == '/qrcode':
        text = '/qrcode https://www.youtube.com/channel/UC92EEOWePEoz09IpI4MZ3Wg'
    text = text.split()
    main.qr_code(text[1], 'qrcode.png')
    with open('qrcode.png', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        os.remove('qrcode.png')
    bot.send_message(message.chat.id, 'Вот Ваш QRCode!! Спасибо за использование!')


@bot.message_handler(commands=['git'])
def git(message):
    bot.send_message(message.chat.id, 'https://github.com/slezkinis/QRcode-on-Telegram')


bot.polling(none_stop=True)

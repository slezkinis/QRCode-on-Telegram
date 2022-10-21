import os

import telebot
from dotenv import load_dotenv

import main


load_dotenv()
telegram_token = os.environ['TG_TOKEN']
bot = telebot.TeleBot(token=telegram_token)
HELP = '''
/help - помощь
/qrcode <ссылка> - получить qrcode
'''


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['qrcode'])
def qrcode(message):
    main.qr_code(message.text, 'qrcode.png')
    with open('qrcode.png', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        os.remove('qrcode.gif')
    bot.send_message(message.chat.id, 'Вот Ваш QRCode!! Спасибо за использование!')


bot.polling(none_stop=True)

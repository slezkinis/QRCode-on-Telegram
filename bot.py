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
    main.qr_code(message.text, 'qrcode.gif')
    with open('qrcode.gif', 'rb') as file:
        bot.send_document(message.chat.id, document=file)
        os.remove('qrcode.gif')
    bot.send_message(message.chat.id, 'Вот Ваш QRCode!! Спасибо за использование!')


bot.polling(none_stop=True)

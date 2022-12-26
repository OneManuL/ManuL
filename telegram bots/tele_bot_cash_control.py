import telebot
import json

config = {
    "name": 'garry_seldon_bot',
    "token": '5626631612:AAFP90Rdn4gPWFsYU_YN_w-B7h9MrGNvD7E'
}
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

button1 = telebot.types.KeyboardButton('Переглянути гаманець')
button2 = telebot.types.KeyboardButton('Додати')
button3 = telebot.types.KeyboardButton('Відняти')
button4 = telebot.types.KeyboardButton('Статистика')

keyboard.add(button1)
keyboard.add(button2)
keyboard.add(button3)
keyboard.add(button4)

sara = telebot.TeleBot(config['token'])

with open('money', 'r', encoding='utf-8') as file:
    file_r = json.load(file)


@sara.message_handler(content_types=['text'])
def get_text(message):
    pass


@sara.message_handler(commands=['start', 'buttons'])
def start(message):
    pass


@sara.callback_query_handler(func=lambda call: True)
def callback_data(call):
    pass






sara.polling(none_stop=True, interval=0)
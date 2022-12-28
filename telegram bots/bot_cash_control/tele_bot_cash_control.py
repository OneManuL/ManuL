import telebot
import json
from random import randint
logo_bad_choie = ['7.png', 'bad_choose.jpg', '103.png', '10.png','107.png','71.png']
logo_start = ['start.jpg', 'images.jpeg']
logo_good_life = ['115.png','114.png','26.png','60.png','91.png','93.png']
logo_add_money = []


config = {
    "name": 'garry_seldon_bot',
    "token": '5626631612:AAFP90Rdn4gPWFsYU_YN_w-B7h9MrGNvD7E'
}
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
#one_time_keyboard=True шоб кнопки зникали

button1 = telebot.types.KeyboardButton('💰 Переглянути гаманець 💰')
button2 = telebot.types.KeyboardButton('✅ Додати ✅')
button3 = telebot.types.KeyboardButton('❌ Відняти ❌')
button4 = telebot.types.KeyboardButton('📈 Статистика 📈')




sara = telebot.TeleBot(config['token'])

ukrainian_one = [False]


@sara.message_handler(commands=['start', 'buttons'])
def start(message):
    if ukrainian_one[0] == False:
        rand = randint(0, len(logo_start)-1)
        with open(f'gif/{logo_start[rand]}', 'rb') as photo:
            sara.send_photo(message.chat.id, photo)
        sara.register_next_step_handler(sara.send_message(message.chat.id, 'Привіт! Введіть правильно, слово - Паляница'), ukrainian_or_no)


@sara.message_handler(content_types=['text'])
def get_text(message):
    try:
        if ukrainian_one[0] == False:
            rand = randint(0, len(logo_start) - 1)
            with open(f'gif/{logo_start[rand]}', 'rb') as photo:
                sara.send_photo(message.chat.id, photo)
            sara.register_next_step_handler(sara.send_message(message.chat.id, 'Введіть слово Паляница🥯'), ukrainian_or_no)
        else:
            if message.text == '💰 Переглянути гаманець 💰':
                sara.register_next_step_handler(sara.send_message(message.chat.id, "Введіть +, якщо любите маму, а ми поки зв'язуємось з банком🏦"), show_money)


            elif message.text == '✅ Додати ✅':
                sara.register_next_step_handler(sara.send_message(message.chat.id, 'Введіть сумму, яку потрібно додати🏦'), add_money)

            elif message.text == '❌ Відняти ❌':
                sara.register_next_step_handler(sara.send_message(message.chat.id, 'Введіть сумму, яку потрібно зняти з рахунку🏦'), fire_money)

            elif message.text == '📈 Статистика 📈':
                rand = randint(0, len(logo_good_life) - 1)
                with open(f'gif/{logo_good_life[rand]}', 'rb') as photo:
                    sara.send_photo(message.chat.id, photo)
                sara.send_message(message.chat.id, 'Вам доступна пробна версія телеграм бота, якщо ви хочете збільшити'
                                                   ' можливості відправте 100грн на картковий рахунок: 5375414127844099')
            else:
                sara.send_message(message.chat.id, 'Окреме спілкування не передбачено🥲')
    except:
        sara.send_message(message.chat.id, 'Неочікуване введення оберіть дію на панелі кнопок🙃')


def ukrainian_or_no(message):
    try:
        if 'паляниця' in message.text.lower():
            ukrainian_one[0] = True
            keyboard.add(button1)
            keyboard.add(button2, button3)
            keyboard.add(button4)
            sara.send_message(message.chat.id, 'Пароль вказано вірно. Вітаємо, Шановний!👍🏻', reply_markup=keyboard)
        else:
            rand = randint(0, len(logo_bad_choie)-1)
            with open(f'gif/{logo_bad_choie[rand]}', 'rb') as photo:
                sara.send_photo(message.chat.id, photo)
                sara.send_message(message.chat.id, 'В доступе отказано, спробуйтє - никогда🖕🏻')
    except:
        sara.send_message(message.chat.id, 'Неочікуване введення🙃')


def show_money(message):
    rand = randint(0, len(logo_good_life) - 1)
    with open(f'gif/{logo_good_life[rand]}', 'rb') as photo:
        sara.send_photo(message.chat.id, photo)
    with open('money.json', 'r', encoding='utf-8') as file:
        file_r = json.load(file)
        sara.send_message(message.chat.id, f"{file_r['money']}грн в гаманці💰")


def add_money(message):
    try:
        with open('money.json', 'r') as file:
            file_r = json.load(file)
            file_r['money'] = int(file_r['money']) + int(message.text)
            with open('money.json', 'w') as file1:
                json.dump(file_r, file1)
        rand = randint(0, len(logo_good_life) - 1)
        with open(f'gif/{logo_good_life[rand]}', 'rb') as photo:
            sara.send_photo(message.chat.id, photo)
        with open('money.json', 'r') as file:
            file_r = json.load(file)
            sara.send_message(message.chat.id, f"Успішно додано! Ваш баланс:{file_r['money']}грн💰")
    except:
        sara.send_message(message.chat.id, 'Неочікуване введення🙃')


def fire_money(message):
    try:
        with open('money.json', 'r') as file:
            file_r = json.load(file)
            file_r['money'] = int(file_r['money']) - int(message.text)
            with open('money.json', 'w') as file1:
                json.dump(file_r, file1)
        rand = randint(0, len(logo_bad_choie) - 1)
        with open(f'gif/{logo_bad_choie[rand]}', 'rb') as photo:
            sara.send_photo(message.chat.id, photo)
        with open('money.json', 'r') as file:
            file_r = json.load(file)
            sara.send_message(message.chat.id, f"Успішно знято з рахунку! Ваш баланс:{file_r['money']}грн💰")
    except:
        sara.send_message(message.chat.id, 'Неочікуване введення🙃')


@sara.callback_query_handler(func=lambda call: True)
def callback_data(call):
    pass


sara.polling(none_stop=True, interval=1)

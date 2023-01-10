import telebot
import json

config = {
    "name": 'xxxxx',
    "token": 'xxxxxxxx'
}
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

button1 = telebot.types.KeyboardButton('Переглянути магазин')
button2 = telebot.types.KeyboardButton('Заново')
button3 = telebot.types.KeyboardButton('Кошик')

keyboard.add(button1)
keyboard.add(button3)
keyboard.add(button2)
koshik = []

with open('shop.json', 'r', encoding='utf-8') as file:
    file_r = json.load(file)
    pars_json_tv_k = [i + '\n' for i in file_r['tv'].get('lover_cost_tv')]
    pars_json_phone_k = [i + '\n' for i in file_r['phone'].get('lover_cost_phone')]
    pars_json_tv_v = [i for i in file_r['tv'].get('lover_cost_tv').values()]
    pars_json_phone_v = [i for i in file_r['phone'].get('lover_cost_phone').values()]
    pars_json_tv_k_o = [i + '\n' for i in file_r['tv'].get('lover_cost_tv')]
    pars_json_phone_k_o = [i + '\n' for i in file_r['phone'].get('lover_cost_phone')]

    for i in range(len(pars_json_tv_k)):
        pars_json_tv_k.insert(i + i, str(pars_json_tv_v[i]))
    for i in range(len(pars_json_phone_k)):
        pars_json_phone_k.insert(i + i, str(pars_json_phone_v[i]))

sara = telebot.TeleBot(config['token'])
shop_log = []


@sara.message_handler(commands=['start', 'buttons'])
def start(message):
    global koshik
    koshik = []
    sara.send_message(message.chat.id, 'Привіт!', reply_markup=keyboard)
    if message.text == '/start':
        keyboard_b = telebot.types.InlineKeyboardMarkup()
        keyboard_b.add(telebot.types.InlineKeyboardButton(text='Відгуки', callback_data='vidguk'),
                       telebot.types.InlineKeyboardButton(text='Написати відгук', callback_data='vidguk_w'))

        sara.send_message(message.chat.id, 'Вас вітає магазин де нічого кроми тєліков і тілфонов немає,'
                                           ' Перегляньте відгуки або натисіть кнопку переглянути магазин',
                          reply_markup=keyboard_b)


@sara.callback_query_handler(func=lambda call: True)
def callback_data(call):
    if call.message:
        if call.data == 'vidguk':
            sara.send_message(call.message.chat.id, "Поки не працює")
            # show_vidguk(call)
        elif call.data == "vidguk_w":
            sara.send_message(call.message.chat.id, "Поки не працює")
            # show_vidguk(call)
        elif call.data == 'buy':
            sara.send_message(call.message.chat.id, "Генеруємо посилання для оплати")
        elif call.data == "koshik":
            sara.send_message(call.message.chat.id, "Товар успішно додано до кошику")


@sara.message_handler(content_types=['text'])
def name(message):
    keyboard_b3 = telebot.types.InlineKeyboardMarkup()
    keyboard_b3.add(telebot.types.InlineKeyboardButton(text='Купити', callback_data='buy'))
    if message.text:
        if message.text == 'Переглянути магазин':
            loading_shop(message)
        elif message.text == 'Сортування':
            sara.send_message(message.chat.id, 'Мало товару для сортування, сорі')
        elif message.text == int:
            show_one(message)
        elif message.text == 'Заново':
            sara.send_message(message.chat.id, 'натисніть на /start')
        elif message.text == 'Кошик':
            sara.send_message(message.chat.id, f"В вашому кошику:🔥 {'🔥'.join([i for i in koshik])}", reply_markup = keyboard_b3)


def loading_shop(message):
    sara.send_message(message.chat.id, f"Телевізори:\n🔥{'🔥'.join([i for i in pars_json_tv_k])}\nТелефони"
                                       f":\n🔥{'🔥'.join([i for i in pars_json_phone_k])}")
    sara.register_next_step_handler(
        sara.send_message(message.chat.id, 'Введіть суму товару, що вас зацікавив в форматі  1899'), show_one)


def show_one(message):
    keyboard_b2 = telebot.types.InlineKeyboardMarkup()
    keyboard_b2.add(telebot.types.InlineKeyboardButton(text='До кошику', callback_data='koshik'))
    if message.text + 'грн' in pars_json_tv_v:
        b = pars_json_tv_v.index(message.text + 'грн')
        sara.send_message(message.chat.id, f'{pars_json_tv_k_o[b]}', reply_markup=keyboard_b2)
        koshik.append(pars_json_tv_k_o[b])
    elif message.text + 'грн' in pars_json_phone_v:
        b = pars_json_phone_v.index(message.text + 'грн')
        sara.send_message(message.chat.id, f'{pars_json_phone_k_o[b]}', reply_markup=keyboard_b2)
        koshik.append(pars_json_phone_k_o[b])
    else:
        print('Error')

def show_vidguk(message):
    try:
        with open('vidguk_r.json', 'r', encoding='utf-8') as file:
            file1 = json.load(file)
            sara.send_message(message.chat.id, f'Відгуки\n {file1}')
    except:
        print('Error')


sara.polling(none_stop=True, interval=0)

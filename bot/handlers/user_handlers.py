import telebot
import logging
from bot.config_data import Slot , Admin, Tutor, Student, admin
logging.basicConfig(level='INFO')
bot = telebot.TeleBot('7062078052:AAHWw9Am8GMAuThzrCOVM_ObDP9T7NJ2AEo')
theme = ''
last_name = ''
first_name = ''
token = None

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    btn1 = telebot.types.KeyboardButton('Добавить преподавателя')
    btn2 = telebot.types.KeyboardButton('Удалить преподавателя')
    btn3 = telebot.types.KeyboardButton('Список преподавателей')
    markup.row(btn1)
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id,'Я готов!', reply_markup=markup)
    bot.register_next_step_handler(message, admin_menu)
def admin_menu(message):
    if message.text == 'Добавить преподавателя':
        add_tutor(message)
    elif message.text == 'Список преподавателей':
        desplay_tutors(message)
    elif message.text == 'Удалить преподавателя':
        delete_tutor(message)
        #добавление тьютора
def add_tutor(message):
    global token, last_name
    token = message.chat.id
    if str(message.chat.id) == admin.token:
        bot.send_message(message.chat.id,f'Привет!\nВведи предмет преподавателя')
        bot.register_next_step_handler(message, get_theme)
    else:
        bot.send_message(message.chat.id,f'У вас нет прав администрирования!')
def get_theme(message):
    global theme
    theme = message.text
    bot.send_message(message.chat.id,f'Запомнил!\nВведи фамилию преподавателя')
    if str(message.chat.id) == admin.token:
        bot.register_next_step_handler(message, get_last_name)
#@bot.message_handler(content_types='text')
def get_last_name(message):
    global last_name
    last_name = message.text
    bot.send_message(message.chat.id,'Отлично! А теперь имя')
    bot.register_next_step_handler(message, get_first_name)
#@bot.message_handler(content_types='text')
def get_first_name(message):
    global token, first_name, last_name
    first_name = message.text
    bot.send_message(message.chat.id,'Готово! Скоро ты сможешь открыть слот для занятий')
    logging.info(f'Добавлен преподаватель {first_name} {last_name}')
    admin.creat_tutor(theme, last_name, first_name, token)
    bot.send_message(admin.token, f'Добавлен преподаватель {first_name} {last_name}')
    start(message)

#просмотр списка преподавателей
@bot.message_handler(commands=['list'])
def desplay_tutors(message):
    bot.send_message(message.chat.id, f'Список преподавателей:\n{admin.desplay_calendary()}')
    start(message)
#удаление преподавателя
@bot.message_handler(commands=['deletetutors'])
def delete_tutor(message):
    bot.send_message(admin.token, f'Введите ID перподавателя для удаления')
    bot.register_next_step_handler(message, delete_complite)
def delete_complite(message):
    admin.del_tutor(f'{message.text}')
    bot.send_message(admin.token, f'Преподаватель удален! Список преподавателей:\n{admin.desplay_calendary()}')
    start(message)


bot.polling(non_stop=True)

#
#@bot.message_handler(content_types='text')
#def input_last_name(message):
#    global last_name
#    last_name = message.text
#    bot.send_message(message.chat.id,'Отлично! А теперь имя')
#    bot.register_next_step_handler(message, input_first_name)
#@bot.message_handler(content_types='text')
#def input_first_name(message):
#    global token, first_name, last_name
#    first_name = message.text
#    bot.send_message(message.chat.id,'Готово! Скоро ты сможешь открыть слот для занятий')
#    logging.info(f'Добавлен преподаватель {first_name} {last_name}')
#    admin.creat_tutor('Информатика', last_name, first_name, token)
#    bot.send_message(admin.token, f'Добавлен преподаватель {first_name} {last_name}')
#if str(message.chat.id) == admin.token:
#else:
#
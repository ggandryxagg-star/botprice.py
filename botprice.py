import telebot
from telebot import * 
import random
import sqlite3


bot = telebot.TeleBot('8540431919:AAElX4EiyLES1CNqjm1ORkkmg8AoCharW1k')


name = None 
last_name = None


@bot.message_handler(commands=[
    'start'
])


def main(message):
    
    con = sqlite3.connect('curs_prog.slllw')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), lst_name varchar(50), cla son varchar(50))')
    con.commit()
    cur.close()
    con.close()

    bot.send_message(message.chat.id, 'Привет, этот бот регистрирует тебя на курс по программированию\nВводите свои достоверные данные иначе вы будете исключены с курса')
    bot.send_message(message.chat.id, 'Введите свое имя:')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    
    global name

    name = message.text.strip()
    
    bot.send_message(message.chat.id, 'Отлично, сейчас нужно будет ввести свою фамилию:')
    bot.register_next_step_handler(message, us_las)

def us_las(message):
    
    global last_name

    last_name = message.text.strip()
    
    bot.send_message(message.chat.id, 'И на последок, нужно будет ввести в каком вы классе:')
    bot.register_next_step_handler(message, lst_name)

def lst_name(message):

    classi = message.text.strip()

    con = sqlite3.connect('curs_prog.slllw')
    cur = con.cursor()
    cur.execute('INSERT INTO users(name, lst_name, clason) VALUES ("%s","%s", "%s")' % (name, last_name, classi))
    con.commit()
    cur.close()
    con.close()

    mark = telebot.types.InlineKeyboardMarkup()
    bt = telebot.types.InlineKeyboardButton('Вернуться в тгк', url='https://t.me/+qwv1ZoFwOz4xMmMy')
    mark.add(bt)

    bot.send_message(message.chat.id, f'Успешная регистрация на курс\nМожете возвращаться в тгк', reply_markup=mark)


@bot.message_handler(commands=['list'])

def listok(message):

    con = sqlite3.connect('curs_prog.slllw')
    cur = con.cursor()
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''

    for sl in users:
        info += f'имя: {sl[1]}, фамилия: {sl[2]}, класс: {sl[3]}\n'

    cur.close()
    con.close()


    bot.send_message(message.chat.id, info)

bot.polling(none_stop=True)
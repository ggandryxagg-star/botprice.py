import telebot
from telebot import *
import random
import json


bot = telebot.TeleBot('7752117905:AAE_T001gb0eDArNk0WGjkIZBkPTV3-NzQ0')


@bot.message_handler(commands=
                     ['start', 
                      ]
                     )

def popi(message):

    bot.send_message(message.chat.id, 'Привет, этот бот опредиляет пидора, если ты хочешь узнать кто пидор, нужно написать имена тех, кто будет учавствовать в рулетке!')

@bot.message_handler(commands=[
    'anton'
])

def stix(message):

    bot.delete_message(message.chat.id, message.message_id)

    bot.send_message(message.chat.id, 'Едет пэпэ через шнейне\nВидит пэпэ в шнейне фа\nСунул пэпэ руку в шнейне\nШнейне пэпэ ватафа')


@bot.message_handler()

def obratka(message):

    if message.text.lower() == 'я против':

        bot.send_message(message.chat.id, 'Это никого не ебет долбан!!!')

    elif message.text.lower() == 'я пидор':

        bot.send_message(message.chat.id, 'я знаю долбаеб, можешь не писать')

    elif message.text.lower() == 'ты пидор':

        bot.send_message(message.chat.id, 'кто обзывается, тот в говне валяется')

    else:
        
        pidori = False
    
        pidori = message.text.lower()
        pidori = json.dumps(pidori)
        pidori = list(pidori.split())

        y = int(len(pidori))

        x = random.randrange(0,y,1)

        pidors = str(pidori[x])
        
        dic = {
        'u0430': 'а', 'u0431': 'б',
        'u0432': 'в', 'u0433': 'г',
        'u0434': 'д', 'u0435': 'е',
        'u0451': 'ё', 'u0436': 'ж',
        'u0437': 'з', 'u0438': 'и',
        'u0439': 'й', 'u043a': 'к',
        'u043b': 'л', 'u043c': 'м',
        'u043d': 'н', 'u043e': 'о',
        'u043f': 'п', 'u0440': 'р',
        'u0441': 'с', 'u0442': 'т',
        'u0443': 'у', 'u0444': 'ф',
        'u0445': 'х', 'u0446': 'ц',
        'u0447': 'ч', 'u0448': 'ш',
        'u0449': 'щ', 'u044a': 'ъ',
        'u044b': 'ы', 'u044c': 'ь',
        'u044d': 'э', 'u044e': 'ю',
        'u044f': 'я',
        }

        slov = ''

        for keys in dic:
            if keys in pidors:


                pidors.replace(keys, dic.get(keys))
                slov += dic.get(keys)


        bot.send_message(message.chat.id, f'Сегоднящгий пидорас: {slov, pidors}\nЕсли не согласен пиши "я против"')


bot.polling(none_stop=True) 
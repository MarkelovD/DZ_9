import telebot
from telebot import types
import datetime
import random
bot = telebot.TeleBot("TOKEN") # токен бота
candy = 150
limit = 28
# меню
@bot.message_handler(commands = ["start"])

def start(message):
    bot.send_message(message.chat.id,'Игра "конфетки!')
    bot.send_message(message.chat.id,"""Игра в конфеты. На столе лежит 150 конфет.
    Игроки ходят по очереди.
    За ход можно взять 1-28 конфет.
    Игрок взявший последнюю конфету побеждает.""")
    bot.send_message(message.chat.id,f'{message.from_user.first_name} введите количество конфет которое хотите взять: ')
    bot.register_next_step_handler(message, game_mode)

def game_mode(message):
    global candy
    global limit
    u_input = message.text

    if not u_input.isdigit(): # проверка на число
            msg = bot.reply_to(message, f'{message.from_user.first_name} вы ввели не цифры, введите пожалуйста цифры')
            bot.register_next_step_handler(msg, game_mode) # повторный запрос на ввод
            return
    if candy>0:


        # блок игрока
        if int(u_input)<=candy and 1<=int(u_input)<=limit:
            candy=candy-int(u_input)
            if candy==0:
                bot.send_message(message.chat.id, f'{message.from_user.first_name} Win')
            bot.send_message(message.chat.id, f'осталось конфет: {candy}')
        else:
            msg = bot.reply_to(message, f'{message.from_user.first_name} вы вышли за лимит, повторите попытку')
            bot.register_next_step_handler(msg, game_mode) # повторный запрос на ввод при превышении лимита
            return

        # блок бота
        if limit>=candy and candy!=0: #добавил интелекта на финале
            bot_candy=candy
        else:
            bot_candy = random.randint(1,limit) 
        if bot_candy<=candy and 1<=bot_candy<=limit:
            bot.send_message(message.chat.id, f'bot взял: {bot_candy}')
            candy=candy-bot_candy
            if candy==0:
                bot.send_message(message.chat.id, f'bot Win')
            bot.send_message(message.chat.id, f'осталось конфет: {candy}')
        bot.register_next_step_handler(message, game_mode)
        


bot.infinity_polling()      # бесконечная работа бота

# https://github.com/amaRambo/python-seminars что то с семинара
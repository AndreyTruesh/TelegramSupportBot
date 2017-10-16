#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

admin=-1
chat_id=-1
password="1010"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Ты что-то пишешь, я пересылаю!")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Я тестовый бот и мало что могу. В любом случае здесь есть команды помимо /help и /start, но они пока известны только девелоперы(Андрею).")

@bot.message_handler(commands=['status'])
def send_welcome(message):
    bot.reply_to(message, "Я онлайн!")

@bot.message_handler(commands=['log'])
def log_in(message):
    str=message.text.split(" ")
    global admin
    if admin!=-1:
        bot.reply_to(message, "Админ уже авторизован.")
    else:
        if len(str)==2:
            if str[1]==password:
                admin=message.chat.id
                bot.reply_to(message, "Вы авторизованы!")
            else:
                bot.reply_to(message, "Неверный пароль.")
        else:
            bot.reply_to(message, "Недостаточно, или слишком много параметров.")

@bot.message_handler(commands=['off'])
def log_off(message):
    global admin
    if (message.chat.id==admin):
        admin=-1
        bot.reply_to(message, "Вы больше не админ")
    else:
        bot.reply_to(message, "Вы и так не авторизованы")
        



@bot.message_handler(regexp="/chat_+\d")
def switch_chat_id(message):
    if (message.chat.id==admin):
        str=message.text.split("_")
        global chat_id
        chat_id=int(str[1])
        bot.reply_to(message, "Переход в чат №"+str[1])
        bot.send_message(chat_id,"Оператор зашел в ваш чат")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): #
    if admin!=-1:    
        if (message.chat.id==admin):
            if chat_id!=-1:
                bot.send_message(chat_id,message.text)
            else:
                bot.send_message(admin,"Вы не находитесь ни в одном чате")
        else:
            text=message.text+"\n"+"Отправил: "+message.from_user.first_name+" "+message.from_user.last_name+"\n"+"/chat_"+str(message.chat.id)
            bot.send_message(admin, text)
    else:
        bot.reply_to(message, "Админа нет онлайн")



if __name__ == '__main__':
     bot.polling(none_stop=True)
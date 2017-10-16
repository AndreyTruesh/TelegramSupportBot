#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.token)

admin=309139274
chat_id=-1

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Есть русский язык!")



@bot.message_handler(regexp="/chat_+\d")
def switch_chat_id(message):
    if (message.chat.id==admin):
        str=message.text.split("_")
        global chat_id
        chat_id=int(str[1])
        bot.reply_to(message, "Переход в чат №"+str[1])
        bot.send_message(chat_id,"Оператор зашел в ваш чатт")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): #
    if (message.chat.id==admin):
        if chat_id!=-1:
            bot.send_message(chat_id,message.text)
        else:
            bot.send_message(admin,"Вы не находитесь ни в одном чате")
    else:
        bot.reply_to(message, "Отправляю сообщение хозяину")
        text=message.text+"\n"+"Отправил: "+message.from_user.first_name+" "+message.from_user.last_name+"\n"+"/chat_"+str(message.chat.id)
        bot.send_message(admin, text)



if __name__ == '__main__':
    bot.polling(none_stop=True)

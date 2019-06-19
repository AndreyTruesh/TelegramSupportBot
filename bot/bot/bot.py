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
    bot.reply_to(message, "Yo, I will transfer your msg to someone")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Hi! I'm test bot and can't do much :d")

@bot.message_handler(commands=['status'])
def send_welcome(message):
    bot.reply_to(message, "I'm online")

@bot.message_handler(commands=['log'])
def log_in(message):
    str=message.text.split(" ")
    global admin
    if admin!=-1:
        bot.reply_to(message, "Admin is logged on")
    else:
        if len(str)==2:
            if str[1]==password:
                admin=message.chat.id
                bot.reply_to(message, "You are logged on.")
            else:
                bot.reply_to(message, "Incorrect pass")
        else:
            bot.reply_to(message, "Wrong command")

@bot.message_handler(commands=['off'])
def log_off(message):
    global admin
    if (message.chat.id==admin):
        admin=-1
        bot.reply_to(message, "You're no longer admin")
    else:
        bot.reply_to(message, "Did not authorized yet")
        



@bot.message_handler(regexp="/chat_+\d")
def switch_chat_id(message):
    if (message.chat.id==admin):
        str=message.text.split("_")
        global chat_id
        chat_id=int(str[1])
        bot.reply_to(message, "Going to chat №"+str[1])
        bot.send_message(chat_id,"Support guy is joined")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): #
    if admin!=-1:    
        if (message.chat.id==admin):
            if chat_id!=-1:
                bot.send_message(chat_id,message.text)
            else:
                bot.send_message(admin,"Choose a chast before type msg")
        else:
            text=message.text+"\n"+"Отправил: "+message.from_user.first_name+" "+message.from_user.last_name+"\n"+"/chat_"+str(message.chat.id)
            bot.send_message(admin, text)
    else:
        bot.reply_to(message, "Support-Gu is not online")



if __name__ == '__main__':
     bot.polling(none_stop=True)

# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot

bot = telebot.TeleBot('key')

@bot.message_handler()
def start(message):
    # print(message)
    # print(message.text)
    # print(message.from_user.first_name)
    # print(message.from_user.last_name)
    messages = {}
    messages[message.id] = message.from_user.first_name, message.from_user.last_name, message.text
    f = open('dict.txt','a')
    f.write(str(messages))
    f.close()

bot.polling()

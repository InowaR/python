# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot
import ast
bot = telebot.TeleBot('key')

@bot.message_handler()
def start(message):
    messages = {
                "first_name" : message.from_user.first_name, 
                "last_name" : message.from_user.last_name,
                "text" : message.text
              }
    
    with open("messages.txt", "a") as f:
        f.write(str(messages) + "\n")

bot.polling()


with open('messages.txt', 'r') as f:
    file = f.readlines()

for i in range(len(file)):
    str = file[i]
    dictionary = ast.literal_eval(str)
    first_name = dictionary["first_name"]
    last_name = dictionary["last_name"]
    text = dictionary["text"]
    print(first_name, last_name, text)

# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос,
# отвечать на него и отправлять ответ обратно пользователю.

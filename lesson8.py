# Задача 1. Напишите бота для техподдержки. Бот должен записывать обращения пользователей в файл.

import telebot
import ast

bot = telebot.TeleBot('key')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, я бот для ответа на ваши вопросы! Напишите вопрос, дождитесь ответа, напишите снова для получения ответа') 

@bot.message_handler()
def start(message):
    messages = {
                'first_name' : message.from_user.first_name, 
                'last_name' : message.from_user.last_name,
                'text' : message.text
              }
    
    with open('messages.txt', 'a') as f:
        f.write(str(messages) + '\n')

bot.polling()


# Создает новый файл answers.txt с ответами на сообщения пользователей

import ast
import json

def make_reply_to_messages():
    with open('messages.txt', 'r') as f:
        messages = f.readlines()
    for i in range(len(messages)):
        str = messages[i]
        dictionary = ast.literal_eval(str)
        print(dictionary)
        print('Сообщение:', dictionary['text'])
        answer = input('Введите ответ на сообщение: ')
        dictionary['text'] = answer
        serialized = json.dumps(dictionary, ensure_ascii=False)
        print(serialized)
        with open('answers.txt', 'a') as f:
            f.write(serialized + '\n') 

make_reply_to_messages()  

# Задача 2. Напишите программу, которая позволяет считывать из файла вопрос,
# отвечать на него и отправлять ответ обратно пользователю.

import telebot
import ast

bot = telebot.TeleBot('key')

def find_question(first_name, last_name):
    with open('messages.txt', 'r') as f:
        messages = f.readlines()
    for i in range(len(messages)):
        str = messages[i]
        dictionary = ast.literal_eval(str)
        if first_name == dictionary['first_name'] and last_name == dictionary['last_name']:
            return dictionary['text']

def find_answer(first_name, last_name):
    with open('answers.txt', 'r') as f:
        answers = f.readlines()
    for i in range(len(answers)):
        str = answers[i]
        dictionary = ast.literal_eval(str)
        if first_name == dictionary['first_name'] and last_name == dictionary['last_name']:
            return dictionary['text']

@bot.message_handler()
def reply(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    answer = find_answer(first_name, last_name)
    question = find_question(first_name, last_name)
    bot.reply_to(message, f'Сообщение пользователя: {question}\nОтвет на сообщение: {answer}')

bot.polling()
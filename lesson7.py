# Задача 1. Создайте пользовательский аналог метода map().

# array = [1, 2, 3, 4, 5]

# def func(element):
#     return element * 2

# def user_map(func, array):
#     new_array = []
#     for element in array:
#         new_array.append(func(element))
#     return new_array

# print(user_map(func, array))


# Задача 2. Создайте декоратор, повторяющий функцию заданное количество раз.

# def repeat_func(times):
#     def procedure(func):
#         def wrapper():
#             for _ in range(times):
#                 func()
#         return wrapper
#     return procedure

# @repeat_func(times=6)
# def func():
#     print("Hello")

# func()


# Задача 3. Добавьте в telegram-бота игру «Угадай числа».
# Бот загадывает число от 1 до 1000. 
# Когда игрок угадывает его, бот выводит количество сделанных ходов.

import telebot;
bot = telebot.TeleBot('key')

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()
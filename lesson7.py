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


import telebot
import random

bot = telebot.TeleBot('key')

@bot.message_handler(commands=['play'])
def play(message):
    bot.send_message(message.chat.id, 'Игра началась! Я загадал число от 1 до 1000. Введи свой вариант:')

    number = random.randint(1, 3)
    tries = 0

    @bot.message_handler(func=lambda m: True)
    def guess(message):
        nonlocal tries
        try:
            guess_number = int(message.text)
        except ValueError:
            bot.send_message(message.chat.id, 'Некорректный ввод. Попробуй еще раз.')
            return

        tries += 1

        if guess_number > number:
            bot.send_message(message.chat.id, 'Мое число меньше. Попробуй еще раз.')
        elif guess_number < number:
            bot.send_message(message.chat.id, 'Мое число больше. Попробуй еще раз.')
        else:
            bot.send_message(message.chat.id, f'Поздравляю! Ты угадал число за {tries} попыток. Чтобы сыграть еще раз, введите команду /play.')
            tries = 0

@bot.message_handler(commands=['play'])
def new_game(message):
    play(message)

bot.polling()
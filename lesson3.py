# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

N = 6
list = [fibonacci(i) for i in range(1, N+1)]
print(list)

# Задача 2. В списке находятся названия фруктов. 
# Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

fruits = ["айва", "авокадо", "абрикос", "апельсин", "мандарин", "яблоко", "вишня", "гранат"]
for fruit in fruits:
    if fruit.startswith("а"):
        print(fruit)

# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. 
# Бот должен, как минимум, отвечать на фразы «привет», «как тебя зовут». 
# Если фраза ему неизвестна, он выводит соответствующую фразу.

import requests
import time

def weather():
    latitude = 44.0486
    longtitude = 43.0594
    key = "859babe04b3085ce5d5fc2539f283d2b"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longtitude}&appid={key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] != "404":
        city = data["name"]
        temperature = data["main"]
        current_temperature = temperature["temp"]
        description = data["weather"]
        weather_description = description[0]["description"]
        return f"{city}, {current_temperature} ℃, {weather_description}"
    
bot_dictionary = {
    "Привет" : "Привет",
    "Как дела?" : "Хорошо",
    "Сколько времени?" : f"Текущее время: {time.ctime()}",
    "Какая погода?" : f"Погода: {weather()}"
}
question = input("Напишите боту: ")
question = question.capitalize()
if question in bot_dictionary:
    print(bot_dictionary[question])
else:
    print("Фраза неизвестна")



# Задача 1. Создайте пользовательский аналог метода map().

array = [1, 2, 3, 4, 5]

def func(element):
    return element * 2

def user_map(func, array):
    new_array = []
    for element in array:
        new_array.append(func(element))
    return new_array

print(user_map(func, array))
    
# Задача 1. Дано натуральное число N.
# Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.

# 60 -> 2, 2, 3, 5

def list_prime_number(N):
    natural_number = N
    nums = []
    i = 2
    while i < N:
        if natural_number % i == 0:
            natural_number /= i
            nums.append(i)
        i += 1
    print(nums)
    prime_nums = []
    j = 0
    while j < len(nums)-1:
        if N % nums[j] != 0:
            j += 1
        N = N / nums[j]
        prime_nums.append(nums[j])
    print(prime_nums)

list_prime_number(60)

# Задача 2. В первом списке находится информация об ассортименте мороженного, 
# во втором списке - информация о том, какое мороженное есть на складе. 
# Выведите названия того товара, который закончился.

# Пример:
# 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»
# 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»

assortment = ["«Сливочное»", "«Бурёнка»", "«Вафелька»", "«Сладкоежка»"]
available_in_stock = ["«Сливочное»", "«Вафелька»", "«Сладкоежка»"]
for ice_cream in assortment:
    if ice_cream not in available_in_stock:
        print(f"Закончилось: {ice_cream}")

print(set(assortment).difference(set(available_in_stock)))

# Задача 3. Выведите число π с заданной точностью. Точность выводится в виде десятичной дроби.

# 3 -> 3.142

import math
print(f"{math.pi:.3f}")


# Задача 4*. Даны два файла, в каждом из которых находится запись многочлена.
# Найдите сумму данных многочленов.
# 1. 5x^2 + 3x
# 2. 3x^2 + x + 8
# 3. Результат: 8x^2 + 4x + 8

a = "5x^2 + 3x"
b = "3x^2 + x + 8"

def first_coefficient(polynomial):
    first = []
    i = 0
    while i < len(polynomial):
        if polynomial[i] == "x":
            break
        first.append(polynomial[i])
        i += 1
    return first

res = first_coefficient(a) + first_coefficient(b)
first = 0
for i in res:
    first += int(i)


def second_coefficient(polynomial):
    second = []
    i = 0
    while i < len(polynomial):
        if polynomial[i] == "+":
            second.append(polynomial[i+2])
            break
        i += 1
    return second

res = second_coefficient(a) + second_coefficient(b)
second = 0
for i in res:
    if i == "x":
        second += 1
    else:
        second += int(i)


def third_coefficient(polynomial):
    third = []
    i = 0
    count = 0
    while i < len(polynomial):
        if polynomial[i] == "+":
            count += 1
        if count == 2:
            third.append(polynomial[i+2])
            break
        i += 1
    return third

res = third_coefficient(a) + third_coefficient(b)
third = 0
for i in res:
    third += int(i)

print(f"{first}x^2 + {second}x + {third}")
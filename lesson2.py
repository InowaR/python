# Задача 1. Напишите программу, которая принимает на вход число N и 
# выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n
 
number = int(input("Введите число N: "))
for i in range(1, number + 1):
    print(fac(i))



# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
print(f"X | Y | Z | (X ∧ Y) | (X ∧ Y) ∨ Z | ¬(X ∧ Y) ∨ Z")
print("--+---+---+---------+-------------+-------------")
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f"{x} | {y} | {z} |    {x ^ y}    |      {(x ^ y) or z}      |       {int(not ((x ^ y) or z))}")



# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ
# первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2
first_string = "one"
second_string = "onetwonine"
letters = []
counts = []
for i in first_string:
    letters.append(i)
    count = 0
    for j in second_string:
        if i == j:
            count += 1
    counts.append(count)
for letter, count in zip(letters, counts):
    print(f"{letter} - {count}")



# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]
N = 3
position = 2
numbers = list(range(-N, N + 1))
print(numbers)
slice = numbers[-position:]
del(numbers[-position:])
for i in reversed(slice):
    numbers.insert(0, i)
print(numbers)
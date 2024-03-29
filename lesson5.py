# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
# Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random
numbers = [random.randint(1,10) for _ in range(10)]
print(numbers)
numbers = list(filter(lambda numbers : numbers > 5, numbers))
print(numbers)

# Задача 2. Дан список случайных чисел. 
# Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

import random
a = [random.randint(1,10) for _ in range(10)]
print(a)

b = []
random_index = random.randint(0, len(a) - 1)
print(f"Стартовый индекс : {random_index}")
b.append(a[random_index])

random_index = random_index + 1
j = 0
while random_index < len(a):
    if a[random_index] > b[j]:
        b.append(a[random_index])
        j += 1
    random_index += 1
print(b)

# Задача 3. Задайте список случайных чисел от 1 до 10. 
# Посчитайте, сколько всего совпадающих элементов есть в списке. 
# Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают 
# Список уникальных элементов [1, 4, 2, 3, 6, 7]

import random
numbers = [random.randint(1, 10) for _ in range(10)]
print(f"Список случайных чисел: {numbers}")
repeat_numbers = len(numbers) - len(set(numbers))
collection = list(set(numbers))
print(f"Уникальных элементов в массиве: {repeat_numbers}")
print(f"Список уникальных элементов: {collection}")

# Задача 4*. (Необязательная). Создайте игру в крестики-нолики.

import os
field = [["-","-","-"], ["-","-","-"], ["-","-","-"]]

def screen():
    i = 0
    while i < 3:
        print(field[i], "\n")
        i += 1

def first_player(x, y):
    field[x][y] = "x"
    screen()

def second_player(x, y):
    field[x][y] = "o"
    screen()

def possible_move(x, y):
    if 0 <= x < 3 and 0 <= y < 3:
        if field[x][y] == "-":
            return True
        return False
    return False

def row(field):
    i = 0
    while i < 3:
        if field[i] == ["x","x","x"]:
            print("Первый игрок выиграл!")
            return True
        if field[i] == ["o","o","o"]:
            print("Второй игрок выиграл!")
            return True
        i += 1
    return False

def column(field):
    i = 0
    while i < 3:
        if field[0][i] == "x" and field[1][i] == "x" and field[2][i] == "x":
            print("Первый игрок выиграл!")
            return True
        if field[0][i] == "o" and field[1][i] == "o" and field[2][i] == "o":
            print("Второй игрок выиграл!")
            return True
        i += 1
    return False

def diagonale(field):
    if field[0][0] == "x" and field[1][1] == "x" and field[2][2] == "x":
        print("Первый игрок выиграл!")
        return True
    if field[2][0] == "x" and field[1][1] == "x" and field[0][2] == "x":
        print("Первый игрок выиграл!")
        return True
    if field[0][0] == "o" and field[1][1] == "o" and field[2][2] == "o":
        print("Второй игрок выиграл!")
        return True
    if field[2][0] == "o" and field[1][1] == "o" and field[0][2] == "o":
        print("Второй игрок выиграл!")
        return True
    return False
    
def check_winner(field):
    if row(field) == True or column(field) == True or diagonale(field) == True:
        return True
    return False

def check_draw(field):
    for row in field:
        for element in row:
            if element == "-":
                return False
    return True

def main():
    winner = False
    while winner == False:    
        screen()
        while True:
            print("Ход 1 игрока:")
            x = int(input("Введите номер ряда (1,2,3): "))
            x-=1
            y = int(input("Введите номер столбца (1,2,3): "))
            y-=1
            os.system('clear')
            if possible_move(x, y) == True:
                first_player(x, y)
                draw = check_draw(field)
                if draw == True:
                    print("Ничья!")
                    winner = True
                    break
                winner = check_winner(field)
                break
            
            else:
                screen()
                print("Ячейка занята или введены неверные номера!")
        if winner == True:
            break

        while True:
            print("Ход 2 игрока:")
            x = int(input("Введите номер ряда (1,2,3): "))
            x-=1
            y = int(input("Введите номер столбца (1,2,3): "))
            y-=1
            os.system('clear')
            if possible_move(x, y) == True:
                second_player(x, y)
                draw = check_draw(field)
                if draw == True:
                    winner = True
                    print("Ничья!")
                    break
                winner = check_winner(field)
                break
            else:
                screen()
                print("Ячейка занята, введите другие номера!")
        if winner == True:
            break

        os.system('clear')
main()


# Задача 5*. (Необязательная). Двумерный массив размером 5х5 заполнен случайными нулями и единицами. 
# Игрок может ходить только по полям, заполненным единицами. 
# Проверьте, существует ли путь из точки [0, 0] в точку [4, 4]
# (эти поля требуется принудительно задать равными единице).

import numpy as np
field = np.zeros(25)
i = 0
while i < 17:        # Количество единиц в массиве
    field[i] += 1
    i += 1
np.random.shuffle(field)
field = field.reshape(5,5)
field = np.pad(field, pad_width=1, mode='constant', constant_values=0)
print("Сгенерированный лабиринт 5x5 с рамкой")
for row in field:
    print(row)

path = []
path = list(reversed(path))

def next_move(i, j):
    while True:
            if field[i+1][j] != 0 and field[i+1][j] != 2:
                field[i+1][j] = 2
                path.append([i, j])
                i+=1
                break
            if field[i][j+1] != 0 and field[i][j+1] != 2:
                field[i][j+1] = 2
                path.append([i, j])
                j+=1
                break
            if field[i-1][j] != 0 and field[i-1][j] != 2:
                field[i-1][j] = 2
                path.append([i, j])
                i-=1
                break
            if field[i][j-1] != 0 and field[i][j-1] != 2:
                field[i][j-1] = 2
                path.append([i, j])
                j-=1
                break
            else: 
                 break
    return i, j


N = 100     # Большое число вызовов проверки соседних клеток 

field[1][1] = 2
i, j = next_move(1, 1)

def call_next_move(N, i, j):
    count = 0
    while count < N:
        i, j = next_move(i, j)
        count += 1
call_next_move(N, i, j)

for element in path:
     i, j = element
     call_next_move(N, i, j)

print("Путь в лабиринте по полям, заполненным единицами")
for row in field:
    print(row)

start = field[1][1]
end = field[5][5]

if start == 2 and end == 2:
     print("Путь есть")
else: 
     print("Нет пути")
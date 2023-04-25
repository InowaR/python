# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

# N = input("Введите натуральное число: ")
# new_string = int(N) + int(2 * N) + int(3 * N)
# print(new_string)

# Задача 2. Задан массив из случайных цифр на 15 элементов. 
# На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, 
# совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

# import random
# random_numbers = [random.randint(1,10) for _ in range(15)]
# print(random_numbers)

random_numbers = [0, 5, 6, 2, 7, 5, 4, 2, 7, 5, 1, 1, 9]

N = [5,4,2]

start_index = []

i = 0
while i < len(random_numbers):
    if random_numbers[i] == N[0]:
        start_index.append(i)
    i += 1

length = len(start_index)
print(start_index)

bool_array = []

def check_sequence(start_point, length):
    array = []
    i = 0
    while i < len(N):
        j = start_point
        while j <= start_point + length:
            if N[i] == random_numbers[j]:
                array.append(j)
            j += 1
        i += 1
    array = sorted(set(array))
    check_array = []
    for i in array:
        check_array.append(random_numbers[i])
    bool_array.append(check_array == N)


for start_point in start_index:
    check_sequence(start_point, length)

print(bool_array)

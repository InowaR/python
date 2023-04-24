# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
# Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8


# import random
# numbers = [random.randint(1,10) for _ in range(10)]
# print(numbers)
# numbers = list(filter(lambda numbers : numbers > 5, numbers))
# print(numbers)

# Задача 2. Дан список случайных чисел. 
# Создайте список, в который попадают числа, описывающие случайную возрастающую последовательность. 
# Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

# import random
# a = [random.randint(1,10) for _ in range(10)]
# print(a)

# b = []
# random_index = random.randint(0, len(a) - 1)
# print(f"Стартовый индекс : {random_index}")
# b.append(a[random_index])

# random_index = random_index + 1
# j = 0
# while random_index < len(a):
#     if a[random_index] > b[j]:
#         b.append(a[random_index])
#         j += 1
#     random_index += 1
# print(b)

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
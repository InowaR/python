import numpy as np

# Задача 1.
# Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

array_of_elements = [1,2,2,1,3,4,5,5,5]
print(array_of_elements)
unique, counts = np.unique(array_of_elements, return_counts=True)
for i, j in zip(unique, counts):
    print(f'Элемент {i} встречается в массиве {j} раз')

# Задача 2. Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.

two_dimensional_array = np.random.randint(2, size=(5, 5))
unique_rows = np.unique(two_dimensional_array, axis=0)
print(two_dimensional_array)
if unique_rows.shape[0] < two_dimensional_array.shape[0]:
    print("В двумерном массиве есть одинаковые строки")
else: 
    print("Одинаковых строк нет")

# Задача 3. Создайте двумерный массив случайного размера. 
# Найдите индексы максимального и минимального элементов в нём.
# Выведите элементы главной диагонали матрицы в виде одномерного массива.

x = np.random.randint(1, 10)
y = np.random.randint(1, 10)
array = np.random.randint(10, size=(x, y))

print(array)
print(f'Максимальный элемент массива имеет индекс: [{np.argmax(array, axis=0)[0]}, {np.argmax(array, axis=1)[0]}]')
print(f'Минимальный элемент массива имеет индекс: [{np.argmin(array, axis=0)[0]}, {np.argmin(array, axis=1)[0]}]')
print(f'Элементы главной диагонали массива: {array.diagonal()}')
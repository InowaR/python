import numpy as np

# Задача 1.
# Дан список элементов. Используя библиотеку NumPy, подсчитайте количество уникальных элементов в нём.

# array_of_elements = [1,2,2,1,3,4,5,5,5]
# print(array_of_elements)
# unique, counts = np.unique(array_of_elements, return_counts=True)
# for i, j in zip(unique, counts):
#     print(f'Элемент {i} встречается в массиве {j} раз')

# Задача 2. Создайте двумерный массив, размером 5х5. Определите, есть ли в нём одинаковые строки.

two_dimensional_array = np.array([[1,1,1],[1,2,1],[1,2,1],[1,1,1]])
unique_rows = np.unique(two_dimensional_array, axis=0)
print(two_dimensional_array)
if unique_rows.shape[0] < two_dimensional_array.shape[0]:
    print("В двумерном массиве есть одинаковые строки")
else: 
    print("Одинаковых строк нет")

# Задача 1. Напишите программу, которая принимает на вход число N и 
# выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# def fac(n):
#     if n == 0:
#         return 1
#     return fac(n-1) * n
 
# number = int(input("Введите число N: "))
# for i in range(1, number + 1):
#     print(fac(i))



# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.
print(f"X | Y | Z | (X ∧ Y) | (X ∧ Y) ∨ Z | ¬(X ∧ Y) ∨ Z")
print("-------------------------------------------------")
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f"{x} | {y} | {z} |    {x ^ y}    |      {(x ^ y) or z}      |        {int(not ((x ^ y) or z))}")

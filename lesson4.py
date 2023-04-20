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


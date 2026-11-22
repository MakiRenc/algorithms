# Задание 8

def count_digits(n):
    n = abs(n) 
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

num = int(input("Введите число: "))
print("Количество цифр =", count_digits(num))
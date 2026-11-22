# Задание 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Введите число для факториала: "))
print("Факториал =", factorial(num))
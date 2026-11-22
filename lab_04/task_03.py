# Задание 3

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

base = float(input("Введите число x: "))
exponent = int(input("Введите степень n: "))
print("Результат =", power(base, exponent))
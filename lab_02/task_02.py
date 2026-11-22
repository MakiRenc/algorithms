# Задание 2

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

minimum = min(a, b, c)

sum_max = (a + b + c) - minimum

print("Сумма двух наибольших =", sum_max)
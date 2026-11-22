# Задание 3

N = int(input("Введите N (> 0): "))

total = 0

for i in range(1, N + 1):
    odd_number = 2 * i - 1
    total = total + odd_number
    print("Текущая сумма:", total)

print("Квадрат числа N =", total)
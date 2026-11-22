# Задание 8

N = int(input("Введите N (> 1): "))

K = 0
total = 0

while total < N:
    K = K + 1
    total = total + K

print("K =", K)
print("Сумма =", total)
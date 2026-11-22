# Задание 2

N = int(input("Введите N (> 0): "))

product = 1.0
multiplier = 1.1

for i in range(N):
    product = product * multiplier
    multiplier = multiplier + 0.1

print("Произведение =", product)
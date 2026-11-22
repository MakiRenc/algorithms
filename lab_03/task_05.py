# Задание 5

A = float(input("Введите A: "))
N = int(input("Введите N (> 0): "))

total = 1.0
current_power = 1.0
sign = -1 

for i in range(1, N + 1):
    current_power = current_power * A
    total = total + (sign * current_power)
    sign = -sign  

print("Результат =", total)
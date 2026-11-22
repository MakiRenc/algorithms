# Задание 4

A = float(input("Введите A: "))
N = int(input("Введите N (> 0): "))

total = 1  
current_power = 1

for i in range(1, N + 1):
    current_power = current_power * A 
    total = total + current_power

print("Сумма =", total)
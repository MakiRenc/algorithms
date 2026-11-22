# Задание 2

N = int(input("Введите N (> 1): "))
A = int(input("Введите первый член A: "))
D = int(input("Введите знаменатель D: "))

arr = []
current = A

for i in range(N):
    arr.append(current)
    current = current * D

print("Массив:", arr)
# Задание 3

N = int(input("Введите N (> 2): "))
A = int(input("Введите A: "))
B = int(input("Введите B: "))

arr = [A, B]

for i in range(2, N):
    current_sum = sum(arr)
    arr.append(current_sum)

print("Массив:", arr)
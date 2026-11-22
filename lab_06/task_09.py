# Задание 9

N = int(input("Введите размер массива N: "))
arr = []
print("Введите элементы массива:")
for i in range(N):
    arr.append(int(input()))

last_local_max_index = -1

for i in range(1, N - 1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        last_local_max_index = i

if last_local_max_index != -1:
    print("Номер последнего локального максимума:", last_local_max_index)
else:
    print("Локальных максимумов нет")
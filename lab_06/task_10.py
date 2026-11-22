# Задание 10

N = int(input("Введите размер массива N: "))
arr = []
print("Введите элементы массива:")
for i in range(N):
    arr.append(int(input()))

found_indices = []

for i in range(N):
    for j in range(i + 1, N):
        if arr[i] == arr[j]:
            found_indices = [i, j]
            break
    if len(found_indices) > 0:
        break

if len(found_indices) > 0:
    print("Номера одинаковых элементов:", found_indices)
else:
    print("Одинаковых элементов не найдено")
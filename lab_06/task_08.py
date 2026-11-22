# Задание 8

N = int(input("Введите размер массива N: "))
arr = []
print("Введите элементы массива:")
for i in range(N):
    arr.append(int(input()))

even_indices_arr = arr[1::2]

if len(even_indices_arr) > 0:
    print("Минимальный элемент с четными номерами =", min(even_indices_arr))
else:
    print("В массиве нет элементов с четными номерами")
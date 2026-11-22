# Задание 5

N = int(input("Введите размер массива N: "))
arr = []
print("Введите элементы массива:")
for i in range(N):
    arr.append(int(input()))

odd_indices = arr[0::2]

even_indices = arr[1::2]
even_indices.reverse()

print("Элементы с нечетными номерами:", odd_indices)
print("Элементы с четными номерами (по убыванию):", even_indices)
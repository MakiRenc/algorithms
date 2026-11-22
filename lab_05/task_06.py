# Задание 6

N = int(input("Введите размер массива N: "))
arr = []
print("Введите элементы массива:")
for i in range(N):
    arr.append(int(input()))

K = int(input("Введите K: "))
L = int(input("Введите L: "))

sub_array = arr[K-1:L]
average = sum(sub_array) / len(sub_array)

print("Среднее арифметическое =", average)
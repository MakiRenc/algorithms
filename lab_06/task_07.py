# Задание 7

N = int(input("Введите размер массива N: "))
arr = []
print("Введите элементы массива:")
for i in range(N):
    arr.append(int(input()))

diff = arr[1] - arr[0]
is_progression = True

for i in range(1, N - 1):
    if arr[i+1] - arr[i] != diff:
        is_progression = False
        break

if is_progression:
    print("Это арифметическая прогрессия. Разность =", diff)
else:
    print(0)
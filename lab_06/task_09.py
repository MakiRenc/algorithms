# Задание 9

M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
print("Введите элементы матрицы по строкам:")
matrix = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(int(input(f"Элемент [{i}][{j}]: ")))
    matrix.append(row)

matrix.sort(key=lambda x: x[0])

print("Результат:")
for row in matrix:
    print(row)
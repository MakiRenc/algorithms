# Задание 8

M = int(input("Введите количество строк M (четное): "))
N = int(input("Введите количество столбцов N (четное): "))
print("Введите элементы матрицы по строкам:")
matrix = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(int(input(f"Элемент [{i}][{j}]: ")))
    matrix.append(row)

half_m = M // 2
half_n = N // 2

for i in range(half_m):
    for j in range(half_n):
        matrix[i][j], matrix[i + half_m][j + half_n] = matrix[i + half_m][j + half_n], matrix[i][j]

print("Результат:")
for row in matrix:
    print(row)
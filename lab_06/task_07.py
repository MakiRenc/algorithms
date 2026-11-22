# Задание 7

M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
print("Введите элементы матрицы по строкам:")
matrix = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(int(input(f"Элемент [{i}][{j}]: ")))
    matrix.append(row)

min_val = float('inf')
max_val = float('-inf')
min_col = max_col = 0

for i in range(M):
    for j in range(N):
        if matrix[i][j] < min_val:
            min_val = matrix[i][j]
            min_col = j
        if matrix[i][j] > max_val:
            max_val = matrix[i][j]
            max_col = j

for i in range(M):
    matrix[i][min_col], matrix[i][max_col] = matrix[i][max_col], matrix[i][min_col]

print("Результат:")
for row in matrix:
    print(row)
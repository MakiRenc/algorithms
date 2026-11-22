# Задание 6

M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
print("Введите элементы матрицы по строкам:")
matrix = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(int(input(f"Элемент [{i}][{j}]: ")))
    matrix.append(row)

for i in range(M):
    row = matrix[i]
    min_idx = row.index(min(row))
    max_idx = row.index(max(row))
    row[min_idx], row[max_idx] = row[max_idx], row[min_idx]

print("Результат:")
for row in matrix:
    print(row)
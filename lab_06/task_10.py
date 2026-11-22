# Задание 10

M = int(input("Введите порядок матрицы M: "))
print("Введите элементы матрицы по строкам:")
matrix = []
for i in range(M):
    row = []
    for j in range(M):
        row.append(int(input(f"Элемент [{i}][{j}]: ")))
    matrix.append(row)

print("Суммы диагоналей:")

for d in range(M):
    total = 0
    for i in range(M - d):
        total += matrix[i + d][i]
    print("Диагональ", d, ":", total)

# Верхние диагонали
for d in range(1, M):
    total = 0
    for i in range(M - d):
        total += matrix[i][i + d]
    print("Диагональ", d, ":", total)
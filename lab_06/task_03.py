# Задание 3

M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
print("Введите элементы матрицы по строкам:")
matrix = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(int(input(f"Элемент [{i}][{j}]: ")))
    matrix.append(row)

min_prod = None
min_col = 0

for j in range(N):
    prod = 1
    for i in range(M):
        prod *= matrix[i][j]
    
    if min_prod is None or prod < min_prod:
        min_prod = prod
        min_col = j

print("Номер столбца:", min_col)
print("Наименьшее произведение:", min_prod)
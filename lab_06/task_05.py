# Задание 5

M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
print("Введите элементы матрицы по строкам:")
matrix = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(int(input(f"Элемент [{i}][{j}]: ")))
    matrix.append(row)

found_col = 0
for j in range(N):
    is_all_odd = True
    for i in range(M):
        if matrix[i][j] % 2 == 0:   
            is_all_odd = False
            break
    if is_all_odd:
        found_col = j
        break

print("Номер столбца (1-based):", found_col + 1 if found_col != 0 else 0)
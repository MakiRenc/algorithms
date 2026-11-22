# Задание 4

M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
print("Введите элементы матрицы по строкам:")
matrix = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(int(input(f"Элемент [{i}][{j}]: ")))
    matrix.append(row)

for j in range(N):
    col = [matrix[i][j] for i in range(M)]
    avg = sum(col) / M
    count = sum(1 for x in col if x > avg)
    print(f"Столбец {j}: элементов больше среднего ({avg:.2f}) = {count}")
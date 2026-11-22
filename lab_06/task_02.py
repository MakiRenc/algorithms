# Задание 2

M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
print("Введите элементы матрицы по строкам:")
matrix = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(int(input(f"Элемент [{i}][{j}]: ")))
    matrix.append(row)

K = int(input("Введите номер строки K: "))

target_row = matrix[K - 1]

sum_row = sum(target_row)
prod_row = 1
for x in target_row:
    prod_row *= x

print("Сумма элементов:", sum_row)
print("Произведение элементов:", prod_row)
# Задание 1

M = int(input("Введите размер матрицы M (нечетное): "))
print("Введите элементы матрицы по строкам:")
matrix = []
for i in range(M):
    row = []
    for j in range(M):
        row.append(int(input(f"Элемент [{i}][{j}]: ")))
    matrix.append(row)

print("Вывод по спирали:")
top, bottom = 0, M - 1
left, right = 0, M - 1

while top <= bottom and left <= right:
    for i in range(top, bottom + 1):
        print(matrix[i][left], end=" ")
    left += 1
    
    for j in range(left, right + 1):
        print(matrix[bottom][j], end=" ")
    bottom -= 1
    
    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][right], end=" ")
        right -= 1
    
    if top <= bottom:
        for j in range(right, left - 1, -1):
            print(matrix[top][j], end=" ")
        top += 1
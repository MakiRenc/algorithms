# Задание 6

A = int(input("Введите A: "))
B = int(input("Введите B (A < B): "))

for num in range(A, B + 1):
    print((str(num) + " ") * num, end="")
    print()  
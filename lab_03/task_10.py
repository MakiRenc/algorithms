# Задание 10

A = int(input("Введите A: "))
B = int(input("Введите B: "))

while A != B:
    if A > B:
        A = A - B
    else:
        B = B - A

print("НОД =", A)
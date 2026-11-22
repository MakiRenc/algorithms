# Задание 6

num = int(input("Введите число от 1 до 999: "))

if num % 2 == 0:
    parity = "четное"
else:
    parity = "нечетное"

if 1 <= num <= 9:
    digits = "однозначное"
elif 10 <= num <= 99:
    digits = "двузначное"
elif 100 <= num <= 999:
    digits = "трехзначное"
else:
    digits = "вне диапазона"

if digits != "вне диапазона":
    print(parity, digits, "число")
else:
    print("Число не входит в диапазон 1-999")
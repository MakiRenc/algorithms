# Задание 5

a = int(input("Введите число a (не ноль): "))
b = int(input("Введите число b (не ноль): "))

a_mod = abs(a)
b_mod = abs(b)

sum_mod = a_mod + b_mod
diff_mod = a_mod - b_mod
prod_mod = a_mod * b_mod
div_mod = a_mod / b_mod

print("Сумма модулей =", sum_mod)
print("Разность модулей =", diff_mod)
print("Произведение модулей =", prod_mod)
print("Частное модулей =", div_mod)
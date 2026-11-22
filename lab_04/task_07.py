# Задание 7

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_sum(n):
    if n == 0:
        return []
    
    for p in range(n, 1, -1):
        if is_prime(p):
            return [p] + prime_sum(n - p)
    
    return []

num = int(input("Введите число: "))
print("Разложение:", " + ".join(map(str, prime_sum(num))))
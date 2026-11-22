# Задание 9

def hanoi(n, source, target, auxiliary):
    if n == 0:
        return
    
    hanoi(n - 1, source, auxiliary, target)
    
    print(f"Переместить диск {n} с {source} на {target}")
    
    hanoi(n - 1, auxiliary, target, source)

n = int(input("Введите количество дисков: "))
hanoi(n, 'A', 'C', 'B') 
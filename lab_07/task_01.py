# Сортировка пузырьком

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
    
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break

user_input = input("Введите числа для сортировки через пробел: ")

arr = list(map(int, user_input.split()))

print("Исходный массив:", arr)
bubble_sort(arr)
print("Отсортированный массив:", arr)
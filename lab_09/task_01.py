# Сортировка выбором 

def selection_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

user_input = input("Введите числа для сортировки через пробел: ")
arr = list(map(int, user_input.split()))

print("Исходный массив:", arr)
selection_sort(arr)
print("Отсортированный массив:", arr)
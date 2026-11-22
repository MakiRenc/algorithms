# Задание 6

def reverse_words(s):
    words = s.split()  
    
    if len(words) <= 1:
        return s
    
    return words[-1] + " " + reverse_words(" ".join(words[:-1]))

text = input("Введите предложение: ")
print("Результат:", reverse_words(text))
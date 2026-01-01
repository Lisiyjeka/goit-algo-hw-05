from core.hash_table import HashTable
from core.binary_search import binary_search
from core.kmp_search import kmp_search
from core.bm_search import boyer_moore_search
from core.rk_search import rabin_karp_search

# ================================
# Тестуємо  хеш-таблицю:
# ================================

def test_hash_table():
    print("Тестуємо нашу хеш-таблицю:")
    H = HashTable(5)
    
    H.insert("apple", 10)
    print("Додали apple: 10")
    
    H.insert("orange", 20)
    print("Додали orange: 20")
    
    H.insert("banana", 30)
    print("Додали banana: 30")
    
    H.insert("pear", 40)
    print("Додали pear: 40")
    
    H.insert("pineapple", 50)
    print("Додали pineapple: 50")
    
    H.delete("apple")
    print("Вилучили apple")
    
    H.delete("orange")
    print("Вилучили orange")
    
    H.delete("banana")
    print("Вилучили banana")
    
    H.delete("pear")
    print("Вилучили pear")
    
    H.delete("pineapple")
    print("Вилучили pineapple")
    
    H.insert("potato", 10)
    print("Додали potato: 10")

    print("apple: ", H.get("apple"))
    print("orange: ", H.get("orange"))
    print("banana: ", H.get("banana"))
    print("pear: ", H.get("pear"))
    print("pineapple: ", H.get("pineapple"))
    print("potato: ", H.get("potato"))


# ================================
# Тестуємо функцію  бінарного пошуку:
# ================================

def test_binary_search():
    x = 7.4
    arr = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
    
    print("Тестуємо нашу бінарну пошукову функцію:")    
    print("Масив: ", arr)
    print("Значення: ", x)

    result = binary_search(arr, x)
    print("Результат: ", result)   # Виведе: 6

# ================================
# Тестуємо  функцію для пошуку підрядка в тексті:
# ================================
import time

with open('data/стаття 1.txt', 'r') as file:
    text_1 = file.read()

with open('data/стаття 2.txt', 'r') as file:
    text_2 = file.read()
    
pattern = "кількість"

def test_kmp_search():
    print("Тестуємо функцію KMP для пошуку підрядка в тексті:")
    print("Текст 1")

    start_time = time.time()
    result = kmp_search(text_1, pattern)
    end_time = time.time()
    print("Результат індекс: ", result)
    print("Результат: ", text_1[result:result + len(pattern)])
    print("Час виконання: ", end_time - start_time)
    
    print("Текст 2")

    start_time = time.time()
    result = kmp_search(text_2, pattern)
    end_time = time.time()
    print("Результат індекс: ", result)
    print("Результат: ", text_2[result:result + len(pattern)])
    print("Час виконання: ", end_time - start_time)
    
def test_bm_search():
    print("Тестуємо функцію Боєра-мура для пошуку підрядка в тексті:")
    print("Текст 1")

    start_time = time.time()
    result = boyer_moore_search(text_1, pattern)
    end_time = time.time()
    print("Результат індекс: ", result)
    print("Результат: ", text_1[result:result + len(pattern)])
    print("Час виконання: ", end_time - start_time)
    
    print("Текст 2")

    start_time = time.time()
    result = boyer_moore_search(text_2, pattern)
    end_time = time.time()
    print("Результат індекс: ", result)
    print("Результат: ", text_2[result:result + len(pattern)])
    print("Час виконання: ", end_time - start_time)
    
def test_rk_search():
    print("Тестуємо функцію Рабіна-Карпа для пошуку підрядка в тексті:")
    print("Текст 1")

    start_time = time.time()
    result = rabin_karp_search(text_1, pattern)
    end_time = time.time()
    print("Результат індекс: ", result)
    print("Результат: ", text_1[result:result + len(pattern)])
    print("Час виконання: ", end_time - start_time)
    
    print("Текст 2")
    
    start_time = time.time()
    result = rabin_karp_search(text_2, pattern)
    end_time = time.time()
    print("Результат індекс: ", result)
    print("Результат: ", text_2[result:result + len(pattern)])
    print("Час виконання: ", end_time - start_time)



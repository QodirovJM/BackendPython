from exceptions import *

# Шаг 9 - Главная функция
def run_all_functions():
    print("Запуск всех функций:")
    
    # Тестируем функции из шага 1
    print("Деление:", divide_numbers(10, 2))
    print("Проверка положительного:", check_positive(5))
    
    # Тестируем функцию из шага 2
    print("Обработка строки:", process_string("hello"))
    
    # Тестируем функцию из шага 3
    print("Квадрат числа:", calculate_square(4))
    
    # Тестируем функции из шага 4
    print("Обработка списка:", process_list([1, 2, 3]))
    print("Проверка имени файла:", check_file_name("test.txt"))
    print("Обработка числа:", process_number(50))
    
    # Тестируем функцию из шага 5
    print("Анализ ввода:", analyze_input("test"))
    
    # Тестируем функцию из шага 7
    print("Проверка значения:", check_value(50))
    
    # Тестируем функции из шага 8
    print("Подсчет символов:", count_chars("hello"))
    print("Умножение:", multiply_numbers(5, 6))
    print("Проверка возраста:", check_age(25))
    
    print("Все функции выполнены успешно!")

if __name__ == "__main__":
    run_all_functions()
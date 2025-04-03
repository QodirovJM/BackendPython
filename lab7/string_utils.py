# Функция 1: Формирование строки с подстановкой значений
def create_bar_order():
    name = input("Введите имя клиента: ")
    drink_count = int(input("Введите количество напитков: "))
    base_string = "Клиент " + name + " заказал " + str(drink_count * 2) + " напитков со скидкой " + str(get_discount()) + "%"
    return base_string

# Вспомогательная функция для функции 1
def get_discount():
    return 15

# Функция 2: Повторение комбинации строк
def repeat_bar_menu():
    menu_part1 = input("Введите первый пункт меню (например, 'Пиво - 300р'): ")
    menu_part2 = input("Введите второй пункт меню (например, 'Виски - 500р'): ")
    full_menu = menu_part1 + " " + menu_part2
    for i in range(3):
        print(full_menu)

# Функция 3: Подсчет вхождений подстроки без учета регистра
def count_cocktail():
    string = input("Введите текст с напитками: ")
    substring = input("Введите название напитка для поиска: ")
    string_lower = string.lower()
    substring_lower = substring.lower()
    count = string_lower.count(substring_lower)
    return count

# Функция 4: Извлечение подстроки между индексами
def get_bar_name_part():
    bar_name = input("Введите название бара: ")
    start = int(input("Введите начальный индекс (больше 0): "))
    end = int(input("Введите конечный индекс (меньше длины строки минус 1): "))
    if start > 0 and end < len(bar_name) - 1:
        return bar_name[start:end]
    else:
        return "Ошибка: индексы вне допустимого диапазона"

# Функция 5: Поиск латинских букв в строках
def find_latin_in_orders():
    orders = []
    count = int(input("Сколько заказов вы хотите ввести? "))
    for i in range(count):
        order = input(f"Введите заказ {i+1}: ")
        orders.append(order)
    latin_count = 0
    result_orders = []
    latin_chars = "ABCEHKMOPTX"  # Латинские буквы, похожие на кириллические
    for order in orders:
        words = order.split()
        has_latin = False
        for word in words:
            for char in word:
                if char.upper() in latin_chars:
                    has_latin = True
                    break
            if has_latin:
                break
        if has_latin:
            latin_count = latin_count + 1
            result_orders.append(order)
    return result_orders, latin_count

# Функция 6: Проверка на палиндром
def is_palindrome():
    text = input("Введите код или название для проверки на палиндром: ")
    text = text.lower()
    return text == text[::-1]

# Функция 7: Удаление лишних пробелов
def clean_order_spaces():
    order = input("Введите заказ с пробелами: ")
    words = order.split()
    clean_text = " ".join(words)
    return len(clean_text)

# Функция 8: Замена окончаний предложений на перенос строки
def split_bar_rules():
    rules = input("Введите правила бара (с точками, воскл. или вопр. знаками): ")
    result = rules.replace(".", "\n").replace("!", "\n").replace("?", "\n")
    return result

# Функция 9.1: Подсчет гласных в строке
def count_vowels():
    bar_name = input("Введите название бара для подсчета гласных: ")
    vowels = "аеёиоуыэюяaeiou"
    count = 0
    for char in bar_name.lower():
        if char in vowels:
            count = count + 1
    return count

# Функция 9.2: Переворот слов в строке
def reverse_words():
    order = input("Введите заказ для переворота слов: ")
    words = order.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

# Функция 9.3: Замена пробелов на дефисы
def dash_bar_menu():
    menu = input("Введите пункты меню через пробел: ")
    return menu.replace(" ", "-")
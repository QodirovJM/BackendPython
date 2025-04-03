from string_utils import *

# Функция 10: Вызов всех функций
def run_all_bar_functions():
    # Вызов функции 1
    order = create_bar_order()
    print("Заказ:", order)

    # Вызов функции 2
    print("\nМеню бара:")
    repeat_bar_menu()

    # Вызов функции 3
    mojito_count = count_cocktail()
    print("\nКоличество упоминаний напитка:", mojito_count)

    # Вызов функции 4
    name_part = get_bar_name_part()
    print("Часть названия:", name_part)

    # Вызов функции 5
    latin_orders, latin_word_count = find_latin_in_orders()
    print("\nЗаказы с латинскими буквами:", latin_orders)
    print("Количество заказов с латинскими буквами:", latin_word_count)

    # Вызов функции 6
    if is_palindrome():
        print("Введённый текст - палиндром!")
    else:
        print("Введённый текст - не палиндром")

    # Вызов функции 7
    clean_length = clean_order_spaces()
    print("Длина заказа без лишних пробелов:", clean_length)

    # Вызов функции 8
    split_rules = split_bar_rules()
    print("\nПравила бара:")
    print(split_rules)

    # Вызов функции 9.1
    vowel_count = count_vowels()
    print("Количество гласных в названии:", vowel_count)

    # Вызов функции 9.2
    reversed_order = reverse_words()
    print("Перевернутый заказ:", reversed_order)

    # Вызов функции 9.3
    dashed_menu = dash_bar_menu()
    print("Меню с дефисами:", dashed_menu)

if __name__ == "__main__":
    run_all_bar_functions()
from list_functions import *
from sort_functions import *
from tuple_functions import *
from dict_functions import *

# Шаг 19
def run_all():
    # Тестовые данные
    drinks = ["Beer", "Wine", "Vodka"]
    prices = [5, 7, 10]
    bar_tuple = ("Beer", 5, "Cold")
    
    bar_dict1 = {"name": "Beer", "price": 5}
    bar_dict2 = {"name": "Wine", "price": 7}
    bar_dict3 = {"price": 10}
    bar_dict4 = {"name": "Vodka", "stock": 20}
    
    bar_inventory = {
        "Beer": {"price": 5, "quantity": 20},
        "Wine": {"price": 7, "quantity": 3},
        "Vodka": {"price": 10, "quantity": 8},
        "Whiskey": {"price": 15, "quantity": 2}
    }

    complex_dict1 = {
        "bar": {
            "menu": {
                "drinks": {
                    "beer": "Lager",
                    "wine": "Red"
                },
                "prices": {
                    "beer": 5
                }
            },
            "staff": {
                "bartender": {
                    "beer": "IPA"
                }
            }
        }
    }

    print("1. Перевёрнутый список:", reverse_list(drinks))
    print("2. Изменённый список:", change_drinks(drinks.copy()))
    print("3. Сравнение списков:", compare_lists(drinks, drinks.copy(), drinks.copy()))
    print("4. Диапазон:", get_range(drinks, 0, 2, 1))
    print("5. Новый список:", create_drinks(3))
    print("6. Добавление:", add_drink(drinks.copy(), "Rum", 1))
    print("7. Объединение:", merge_and_sort(drinks, ["Rum"], ["Gin"], True))
    print("8. Проверка длины:", check_length())
    print("9. Добавление с порогом:", add_lists(drinks.copy(), ["Rum"], ["Gin"], 4))
    print("10.1 Сортировка по длине:", sort_by_length(drinks))
    print("10.2 Сортировка по имени:", sort_by_name(drinks))
    print("10.3 Сортировка наоборот:", sort_by_reverse(drinks))
    print("10.4 Сортировка верхний регистр:", sort_upper(drinks))
    print("10.5 Сортировка по длине (map):", sort_length_map(drinks))
    print("10.6 Сортировка по первой букве:", sort_first_letter(drinks))
    temp_list = drinks.copy()
    print("11. Минимальный элемент:", get_min(temp_list))
    print("12. Сумма кортежей:", tuple_count(bar_tuple, bar_tuple))
    print("13. Типы данных:", get_types(bar_tuple))
    print("14. Поиск в кортеже:", find_in_tuple(bar_tuple, "Beer"))
    print("15. 2D список:", make_2d_list(drinks, prices))
    print("16.1 Общая стоимость запасов:", calculate_inventory_value(bar_inventory))
    print("16.2 Напитки с низким запасом:", get_low_stock_drinks(bar_inventory, 5))
    print("16.3 Общее количество единиц:", get_total_stock(bar_inventory))    
    print("17. Подсчёт ключа (3 словаря):", count_key(bar_dict1, bar_dict2, bar_dict3, key="name"))
    print("17. Подсчёт ключа (4 словаря):", count_key(bar_dict1, bar_dict2, bar_dict3, bar_dict4, key="name"))
    print("17. Подсчёт ключа (с minimum):", count_key(bar_dict1, bar_dict2, bar_dict3, key="name", min_occurrences=3))
    print("18. Глубокий поиск:", find_deepest(complex_dict1, "beer"))

if __name__ == "__main__":
    run_all()
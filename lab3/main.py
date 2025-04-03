import bar_functions

if __name__ == "__main__":
    # Функция без параметров
    print(bar_functions.welcome_to_bar())

    # Функция с параметрами
    print(bar_functions.get_drink_name("Виски"))

    # Функция с параметрами по умолчанию
    print(bar_functions.describe_drink())
    print(bar_functions.describe_drink("Водка", 40))

    # Функция с типами
    print(bar_functions.set_drink_price("Пиво", 150.0))

    # Функция с *args
    print(bar_functions.list_drinks("Ром", "Текила", "Джин"))

    # Функция с **kwargs
    print(bar_functions.drink_details(name="Маргарита", type="Коктейль", price=250))

    # Функция, вызывающая другую функцию
    print(bar_functions.announce_drink("Кровавая Мэри"))

    # Функция с функцией как параметр (пример 1)
    print(bar_functions.apply_discount(bar_functions.set_drink_price, 15))

    # Функция с функцией как параметр (пример 2)
    print(bar_functions.format_drink_name(bar_functions.get_drink_name, "Эль"))

    # Функция с функцией как параметр (пример 3)
    def availability_check(name):
        return f"{name} есть в наличии"
    print(bar_functions.check_drink(availability_check, "Коньяк"))

    # Функция с локальной функцией (пример 1)
    print(f"Количество заказов: {bar_functions.order_counter()}")

    # Функция с локальной функцией (пример 2)
    print(bar_functions.drink_info("Лонг Айленд"))

    # Лямбда без параметров
    print(bar_functions.no_param_lambda())

    # Лямбда с параметрами
    print(bar_functions.add_volume_lambda("Шот", 50))

    # Функция с лямбда-выражением
    result = bar_functions.process_drink(bar_functions.add_volume_lambda, "Саке", 200)
    print(result)

    # Замыкания (пример 1)
    tip_10 = bar_functions.create_tip_calculator(10)
    print(f"Чаевые: {tip_10(500)} рублей")

    # Замыкания (пример 2)
    cocktails = bar_functions.drink_category("Коктейли")
    print(cocktails("Космополитен"))

    # Замыкания (пример 3)
    adjust_price = bar_functions.price_modifier(200)
    print(f"Новая цена: {adjust_price(30)} рублей")
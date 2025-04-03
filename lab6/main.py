from bar_data import test_imports, get_drink_info, add_order_to_dict, create_new_drink
from customers import add_customer_to_list, update_customer_spent
from drinks import add_drink, check_drink_stock, format_drink_price
from cocktails import get_cocktail_price, mix_cocktail, random_cocktail
from ingredients import count_ingredients, check_ingredient_cost, random_ingredient
from staff import get_bartender_name, format_staff_salary, calculate_shift_hours
from orders import process_order, format_order_number, create_order
from data_classes import BarDrink, BarCustomer, BarOrder

# Шаг 10: Главная функция
def run_bar_system():
    print("Запускаем бар!")

    # Шаг 2: Демонстрация импортов
    print("Проверяем работу всех модулей:")
    print(test_imports())

    # Шаг 4: Функции с random
    print("\nСлучайно выбираем коктейль:")
    print(f"Случайно был выбран коктейль: {random_cocktail()}")
    print("Случайно выбираем количество ингредиентов:")
    print(f"Случайное количество ингредиентов: {random_ingredient()}")

    # Шаг 5: Функции с math
    print("\nДобавляем напиток с учетом скидки:")
    print(add_drink("Лимонад", 150))
    print("Проверяем запас напитков для парного количества:")
    print(f"Необходимо закупить: {check_drink_stock(7)} пар")
    print("Считаем корень из часов смены бармена:")
    print(f"Результат вычисления: {calculate_shift_hours(16)}")

    # Шаг 6: Функции с locale
    print("\nФорматируем цену напитка в рублях:")
    print(f"Цена напитка: {format_drink_price(200)}")
    print("Форматируем зарплату бармена:")
    print(f"Зарплата: {format_staff_salary(30000)}")
    print("Форматируем номер заказа с разделителями:")
    print(f"Номер заказа: {format_order_number(12345)}")

    # Шаг 7: Функции с decimal
    print("\nСчитаем точную цену коктейля с наценкой:")
    print(f"Итоговая цена: {get_cocktail_price(100)}")
    print("Считаем стоимость ингредиента с наценкой:")
    print(f"Стоимость с наценкой: {check_ingredient_cost(50)}")

    # Шаг 9: Функции с data-классами
    print("\n Получаем информацию о напитке:") 
    drink = BarDrink("Кола", 80)
    print(get_drink_info(drink))

    print("Добавляем клиента в список:")
    customer = BarCustomer("Петя", 0)
    print(f"Список клиентов: {add_customer_to_list(customer)}")

    print("Добавляем заказ в словарь:")
    order = BarOrder(1, "Мохито")
    print(f"Словарь заказов: {add_order_to_dict(order)}")

    print("Обновляем сумму, потраченную клиентом:")
    updated_customer = update_customer_spent(customer, 100)
    print(f"Клиент {updated_customer.name} теперь потратил: {updated_customer.spent}")

    print("Создаем новый напиток:")
    new_drink = create_new_drink("Вода", 50)
    print(f"Создан напиток: {new_drink.name} с ценой {new_drink.price}")

if __name__ == "__main__":
    run_bar_system()
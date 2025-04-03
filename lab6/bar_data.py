from drinks import add_drink
from cocktails import get_cocktail_price
from ingredients import count_ingredients
from staff import get_bartender_name
from orders import process_order
from customers import get_customer_info
from data_classes import BarDrink, BarOrder  # Импортируем из нового файла

# Шаг 9.1: Передача объекта data-класса как параметр
def get_drink_info(drink_obj):
    return f"Напиток: {drink_obj.name}, цена: {drink_obj.price}"

# Шаг 9.3: Работа со словарем объектов data-класса
def add_order_to_dict(order_obj):
    orders_dict = {}
    orders_dict[order_obj.order_id] = order_obj
    return orders_dict

# Шаг 9.5: Создание объекта data-класса
def create_new_drink(name, price):
    return BarDrink(name=name, price=price)

# Шаг 2: Демонстрация импортов
def test_imports():
    drink = add_drink("Сок", 100)
    price = get_cocktail_price(50)
    ing = count_ingredients(5)
    bartender = get_bartender_name()
    order = process_order(123)
    customer = get_customer_info("Вася")
    return f"{drink}, {price}, {ing}, {bartender}, {order}, {customer}"
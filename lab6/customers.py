from data_classes import BarDrink, BarCustomer, BarOrder  # Импортируем из нового файла

def get_customer_info(name):
    return f"Клиент: {name}"

def add_customer_to_list(customer_obj):
    # Шаг 9.2: Работа со списком объектов data-класса
    customers_list = []
    customers_list.append(customer_obj)
    return customers_list

def update_customer_spent(customer_obj, amount):
    # Шаг 9.4: Модификация объекта data-класса
    customer_obj.spent += amount
    return customer_obj
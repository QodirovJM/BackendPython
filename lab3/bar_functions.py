# Функция без параметров
def welcome_to_bar():
    return "Добро пожаловать в бар!"

# Функция с параметрами
def get_drink_name(name):
    return f"Напиток: {name}"

# Функция с несколькими параметрами со значениями по умолчанию
def describe_drink(type="Коктейль", alcohol_percent=10):
    return f"Тип: {type}, Крепость: {alcohol_percent}%"

# Функция с несколькими параметрами, у которых задан тип
def set_drink_price(name: str, price: float) -> str:
    return f"Напиток '{name}' стоит {price} рублей"

# Функция с неопределённым количеством параметров (*args)
def list_drinks(*drink_names):
    return "Доступные напитки: " + ", ".join(drink_names)

# Функция с неопределённым количеством параметров (**kwargs)
def drink_details(**info):
    details = ""
    for key, value in info.items():
        details += f"{key}: {value}, "
    return details[:-2]  # Убираем последнюю запятую и пробел

# Функция, вызывающая внутри себя другую функцию
def announce_drink(drink):
    greeting = welcome_to_bar()
    return f"{greeting} Ваш напиток: {drink}"

# Функция, принимающая функцию как параметр (пример 1)
def apply_discount(get_price_func, discount):
    price = float(get_price_func("Мохито", 300.0).split()[-2])
    new_price = price - (price * discount / 100)
    return f"Цена со скидкой: {new_price} рублей"

# Функция, принимающая функцию как параметр (пример 2)
def format_drink_name(format_func, name):
    return format_func(name)

# Функция, принимающая функцию как параметр (пример 3)
def check_drink(check_func, name):
    return f"Статус напитка: {check_func(name)}"

# Функция с локальной функцией (пример 1)
def order_counter():
    count = 0
    def increase_order():
        nonlocal count
        count += 1
        return count
    return increase_order()

# Функция с локальной функцией (пример 2)
def drink_info(drink):
    def add_status():
        return f"Напиток - {drink} готов"
    return add_status()

# Лямбда-выражение без параметров
no_param_lambda = lambda: "Бар открыт!"

# Лямбда-выражение с параметрами
add_volume_lambda = lambda name, volume: f"{name} ({volume} мл)"

# Функция, принимающая лямбда-выражение как параметр
def process_drink(lambda_func, name, value):
    return lambda_func(name, value)

# Функция с замыканиями (пример 1)
def create_tip_calculator(tip_percent):
    def calculate_tip(amount):
        return amount * tip_percent / 100
    return calculate_tip

# Функция с замыканиями (пример 2)
def drink_category(category):
    def add_category(name):
        return f"{name} из категории {category}"
    return add_category

# Функция с замыканиями (пример 3)
def price_modifier(base_price):
    def modify(amount):
        return base_price + amount
    return modify
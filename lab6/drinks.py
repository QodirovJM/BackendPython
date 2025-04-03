from cocktails import get_cocktail_price, mix_cocktail

def add_drink(name, price):
    # Шаг 5: Используем math
    import math
    discounted_price = math.floor(price * 0.9)  # Скидка 10%
    return f"Напиток {name} добавлен со скидкой: {discounted_price}"

def check_drink_stock(amount):
    # Шаг 5: Используем math
    import math
    return math.ceil(amount / 2)  # Округляем вверх для парного количества

def format_drink_price(price):
    # Шаг 6: Используем locale
    import locale
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    return locale.currency(price, grouping=True)
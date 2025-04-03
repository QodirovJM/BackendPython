from staff import get_bartender_name

def count_ingredients(amount):
    return f"Ингредиентов в наличии: {amount}"

def check_ingredient_cost(cost):
    # Шаг 7: Используем decimal
    from decimal import Decimal
    return Decimal(str(cost)) * Decimal('1.2')  # Наценка 20%

def random_ingredient():
    # Шаг 4: Используем random
    import random
    return random.randint(1, 10)  # Случайное количество ингредиентов
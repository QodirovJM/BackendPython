from ingredients import count_ingredients

def get_cocktail_price(base_price):
    # Шаг 7: Используем decimal
    from decimal import Decimal
    return Decimal(str(base_price)) + Decimal('5.50')

def mix_cocktail(name, strength):
    return f"Смешан коктейль {name} с крепостью {strength}%"

def random_cocktail():
    # Шаг 4: Используем random
    import random
    cocktails = ["Мохито", "Маргарита", "Пина Колада"]
    return random.choice(cocktails)
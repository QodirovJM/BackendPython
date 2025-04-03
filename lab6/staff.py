from orders import process_order

def get_bartender_name():
    return "Игорь"

def format_staff_salary(salary):
    # Шаг 6: Используем locale
    import locale
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    return locale.currency(salary, grouping=True)

def calculate_shift_hours(hours):
    # Шаг 5: Используем math
    import math
    return math.sqrt(hours)  # Просто пример
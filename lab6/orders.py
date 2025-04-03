from customers import get_customer_info

def process_order(order_id):
    return f"Заказ #{order_id} обработан"

def format_order_number(number):
    # Шаг 6: Используем locale
    import locale
    locale.setlocale(locale.LC_ALL, 'ru_RU')
    return locale.format_string("%d", number, grouping=True)

def create_order(customer, drink):
    return f"Заказ для {customer}: {drink}"
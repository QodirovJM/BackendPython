# Работа со словарями
# Шаг 16 - Функция 1: Считаем общую стоимость запасов
def calculate_inventory_value(bar_dict):
    total = 0
    for drink in bar_dict:
        if "price" in bar_dict[drink] and "quantity" in bar_dict[drink]:
            price = bar_dict[drink]["price"]
            quantity = bar_dict[drink]["quantity"]
            total = total + (price * quantity)
    return total

# Шаг 16 - Функция 2: Ищем напитки с маленьким запасом
def get_low_stock_drinks(bar_dict, threshold):
    low_drinks = []
    for drink in bar_dict:
        if "quantity" in bar_dict[drink]:
            if bar_dict[drink]["quantity"] < threshold:
                low_drinks.append(drink)
    return low_drinks

# Шаг 16 - Функция 3: Подсчёт общего количества единиц товара
def get_total_stock(bar_dict):
    total_stock = 0
    for drink in bar_dict:
        if "quantity" in bar_dict[drink]:
            total_stock = total_stock + bar_dict[drink]["quantity"]
    return total_stock

# Шаг 17
def count_key(*dicts, key, min_occurrences=1):
    total_count = 0
    for d in dicts:
        if key in d:
            total_count += 1
    
    if total_count < min_occurrences:
        return f"Ключ '{key}' встречается {total_count} раз, что меньше минимального значения {min_occurrences}"
    return total_count

# Шаг 18
def find_deepest(bar_dict, search_key):
    def recursive_search(current_dict, depth=0, max_depth_values=None):
        if max_depth_values is None:
            max_depth_values = {"depth": 0, "values": []}
        
        # Если это не словарь, прекращаем рекурсию
        if not isinstance(current_dict, dict):
            return max_depth_values
        
        # Проверяем текущий уровень
        for key, value in current_dict.items():
            if key == search_key and not isinstance(value, dict):
                # Если нашли ключ и значение не словарь, обновляем максимальную глубину
                if depth >= max_depth_values["depth"]:
                    if depth > max_depth_values["depth"]:
                        max_depth_values["values"] = []
                        max_depth_values["depth"] = depth
                    max_depth_values["values"].append(value)
            # Если значение - словарь, продолжаем рекурсию
            elif isinstance(value, dict):
                max_depth_values = recursive_search(value, depth + 1, max_depth_values)
        
        return max_depth_values
    
    # Запускаем рекурсивный поиск
    result = recursive_search(bar_dict)
    
    # Если ничего не нашли или глубина 0, возвращаем None
    if not result["values"] or result["depth"] < 3:
        return None
    # Возвращаем список значений на максимальной глубине
    return result["values"]
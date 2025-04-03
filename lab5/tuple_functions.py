# Шаг 12 - работа с кортежами
def tuple_count(tuple1, tuple2):
    total = len(tuple1) + len(tuple2)
    return total

def tuple_check(tuple1, item):
    return item in tuple1

# Шаг 13
def get_types(input_tuple):
    types_tuple = tuple(type(x) for x in input_tuple)
    return types_tuple

# Шаг 14
def find_in_tuple(bar_tuple, item):
    if item in bar_tuple:
        return "Есть в кортеже"
    return "Нет в кортеже"
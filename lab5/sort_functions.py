# Шаг 10 - сортировки (6 функций, 3 с map)
def sort_by_length(drinks_list):
    return sorted(drinks_list, key=len)

def sort_by_name(drinks_list):
    return sorted(drinks_list)

def sort_by_reverse(drinks_list):
    return sorted(drinks_list, reverse=True)

def sort_upper(drinks_list):  # с map
    upper_list = list(map(str.upper, drinks_list))
    return sorted(upper_list)

def sort_length_map(drinks_list):  # с map
    lengths = list(map(len, drinks_list))
    return sorted(drinks_list, key=len)

def sort_first_letter(drinks_list):  # с map
    first_letters = list(map(lambda x: x[0], drinks_list))
    return sorted(drinks_list, key=lambda x: x[0])
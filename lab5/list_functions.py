# Шаг 1
def reverse_list(drinks_list):
    new_list = drinks_list[::-1]
    return new_list

# Шаг 2
def change_drinks(drinks_list):
    for i in range(len(drinks_list)):
        drinks_list[i] = drinks_list[i] + " cold"
    return drinks_list

# Шаг 3
def compare_lists(list1, list2, list3):
    if list1 == list2 and list2 == list3:
        return "Все списки одинаковые"
    else:
        return "Списки разные"

# Шаг 4
def get_range(drinks_list, start, end, step):
    if start < 0 or end > len(drinks_list) or step <= 0:
        return "Ошибка в параметрах"
    new_list = drinks_list[start:end:step]
    return new_list

# Шаг 5
def create_drinks(count):
    drinks = []
    for i in range(count):
        drinks.append("Beer " + str(i + 1))
    return drinks

# Шаг 6
def add_drink(drinks_list, drink, position):
    if position < 0 or position > len(drinks_list):
        return "Неправильная позиция"
    drinks_list.insert(position, drink)
    return drinks_list

# Шаг 7
def merge_and_sort(list1, list2, list3, reverse=False):
    big_list = list1 + list2 + list3
    if reverse:
        big_list.sort(reverse=True)
    else:
        big_list.sort()
    return big_list

# Шаг 8
def check_length():
    import random
    length = random.randint(5, 10)
    numbers = []
    for i in range(length):
        numbers.append(i)
    
    if len(numbers) % 2 == 0:
        print("Чётная длина, делаем нечётную")
        while len(numbers) % 2 == 0:
            numbers.pop()
    else:
        middle = len(numbers) // 2
        middle_value = numbers[middle]
        count = 0
        for num in numbers:
            if num == middle_value:
                count += 1
        print(f"Центральный элемент {middle_value}, таких элементов: {count}")
    return numbers

# Шаг 9
def add_lists(main_list, list1, list2, max_length):
    main_list.extend(list1)
    main_list.extend(list2)
    while len(main_list) > max_length:
        main_list.pop()
    return main_list

# Шаг 11
def get_min(drinks_list):
    if not drinks_list:
        return "Список пустой"
    min_drink = min(drinks_list)
    drinks_list.remove(min_drink)
    return min_drink

# Шаг 15
def make_2d_list(drinks, prices):
    bar_menu = []
    for i in range(len(drinks)):
        bar_menu.append([drinks[i], prices[i]])
    return bar_menu
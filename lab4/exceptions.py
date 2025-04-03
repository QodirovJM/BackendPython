# Шаг 1 - Функции без обработчиков исключений
def divide_numbers(a, b):
    if b == 0:
        raise ZeroDivisionError("Деление на ноль!")
    return a / b

def check_positive(number):
    if number < 0:
        raise ValueError("Число должно быть положительным!")
    return number

# Шаг 2 - Функция с одним обработчиком Exception
def process_string(text):
    if not isinstance(text, str):
        raise TypeError("Нужна строка!")
    try:
        length = len(text)
        if length == 0:
            raise ValueError("Строка пустая!")
    except Exception as e:
        print(f"Ошибка: {e}")
        return 0
    return length

# Шаг 3 - Функция с обработчиком и finally
def calculate_square(number):
    if not isinstance(number, int):
        raise TypeError("Нужно целое число!")
    try:
        if number < 0:
            raise ValueError("Число отрицательное!")
        result = number * number
    except Exception as e:
        print(f"Поймано исключение: {e}")
        return -1
    finally:
        print("Завершение вычисления квадрата")
    return result

# Шаг 4 - Функции с несколькими обработчиками
def process_list(my_list):
    try:
        if not isinstance(my_list, list):
            raise TypeError("Нужен список!")
        if len(my_list) == 0:
            raise ValueError("Список пуст!")
        if "error" in my_list:
            raise KeyError("Найдена ошибка в списке!")
    except TypeError as e:
        print(f"Ошибка типа: {e}")
        return []
    except ValueError as e:
        print(f"Ошибка значения: {e}")
        return [0]
    except KeyError as e:
        print(f"Ошибка ключа: {e}")
        return None
    return my_list

def check_file_name(filename):
    try:
        if not isinstance(filename, str):
            raise TypeError("Имя файла должно быть строкой!")
        if "." not in filename:
            raise ValueError("Нет расширения файла!")
        if len(filename) > 20:
            raise NameError("Слишком длинное имя!")
    except TypeError as e:
        print(f"Тип ошибки: {e}")
        return "default.txt"
    except ValueError as e:
        print(f"Значение ошибки: {e}")
        return "file.txt"
    except NameError as e:
        print(f"Имя ошибки: {e}")
        return "short.txt"
    finally:
        print("Проверка имени завершена")
    return filename

def process_number(num):
    try:
        if not isinstance(num, (int, float)):
            raise TypeError("Нужно число!")
        if num < 0:
            raise ValueError("Число отрицательное!")
        if num > 1000:
            raise OverflowError("Число слишком большое!")
    except TypeError as e:
        print(f"Ошибка типа: {e}")
        return 0
    except ValueError as e:
        print(f"Ошибка значения: {e}")
        return 1
    except OverflowError as e:
        print(f"Переполнение: {e}")
        return 1000
    return num

# Шаг 6 - Пользовательские исключения
class TooSmallError(Exception):
    pass

class TooBigError(Exception):
    pass

class WrongTypeError(Exception):
    pass

# Шаг 7 - Функция с пользовательским исключением
def check_value(value):
    try:
        if value < 10:
            raise TooSmallError("Значение слишком маленькое!")
        if value > 100:
            raise TooBigError("Значение слишком большое!")
    except TooSmallError as e:
        print(f"Ошибка: {e}")
        return 10
    except TooBigError as e:
        print(f"Ошибка: {e}")
        return 100
    finally:
        print("Проверка значения завершена")
    return value

# Шаг 8 - Дополнительные функции
def count_chars(text):
    try:
        if not text:
            raise ValueError("Текст пустой!")
        if len(text) > 50:
            raise OverflowError("Текст слишком длинный!")
    except ValueError as e:
        print(f"Ошибка: {e}")
        return 0
    except OverflowError as e:
        print(f"Ошибка: {e}")
        return 50
    return len(text)

def multiply_numbers(a, b):
    try:
        if a == 0 or b == 0:
            raise ValueError("Одно из чисел равно нулю!")
        result = a * b
        if result > 10000:
            raise OverflowError("Результат слишком большой!")
    except ValueError as e:
        print(f"Ошибка: {e}")
        return 0
    except OverflowError as e:
        print(f"Ошибка: {e}")
        return 10000
    return result

def check_age(age):
    try:
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным!")
        if age > 150:
            raise ValueError("Слишком большой возраст!")
    except ValueError as e:
        print(f"Ошибка возраста: {e}")
        return 25
    return age

# Шаг 5 - Функция с генерацией исключений
def analyze_input(data):
    try:
        if not data:
            raise ValueError("Данные пустые!")
        if isinstance(data, str) and len(data) > 10:
            raise TooBigError("Строка слишком длинная!")
        if isinstance(data, int) and data < 0:
            raise TooSmallError("Число слишком маленькое!")
    except ValueError as e:
        print(f"Ошибка значения: {e}")
        return "default"
    except TooBigError as e:
        print(f"Слишком большое: {e}")
        return "short"
    except TooSmallError as e:
        print(f"Слишком маленькое: {e}")
        return 0
    finally:
        print("Анализ завершен")
    return data
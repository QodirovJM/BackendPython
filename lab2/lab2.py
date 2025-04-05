#Создание функции
def run_bar_function():
    #присваивание
    x = 10
    y = x + 1

    #преобразование
    x = '5'
    y = int(x)
    z = str(55)

    #Условный оператор
    coctail = input("Введите коктейль: ")
    if coctail == "Джин-тоник":
        print(f"Ваш {coctail} содержит 50мл Джина и 50мл Тоника")
    elif coctail == "Виски-Кола":
        print(f"Ваш {coctail} содержит 50мл Виски и 50мл Кола")
    else:
        print("Вашего заказа нет в меню")

    #Оператор Цикла
    bottle = int(input("Введите объем бутылки Виски:"))
    while bottle > 0:
        bottle -= 50
        print(f"Гость заказал шот Виски. Остаток {bottle}")
        
    for i in range(12):
        print(f"Бар открыт уже {i} час")

#Вызов функции
run_bar_function()
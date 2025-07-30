def multiplication_table():
    # Получаем число, для которого нужна таблица
    num = int(input("Введите число для таблицы умножения: "))

    # Цикл перебирает числа от 1 до 10
    for i in range (1, 11):
        # Вычисляем произведение и выводим его
        result = i * num
        # Используем f-строку для красивого вывода
        print(f"{num} x {i} = {result}")

multiplication_table()
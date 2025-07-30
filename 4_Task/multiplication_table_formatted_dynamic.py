def multiplication_table_formatted_dynamic():
    try:
        num = int(input("Введите число для таблицы умножения: "))
        limit = int(input("До какого числа (например, 10 или 20) вывести таблицу: "))

        if limit <= 0:
            print("Лимит должен быть положительным числом.")
            return

        print(f"\nТаблица умножения для {num} до {limit}:")

        # Определяем максимальную ширину для каждого столбца, чтобы все было выровнено
        max_num_len = len(str(num))
        max_i_len = len(str(limit))
        max_result_len = len(str(num * limit))

        for i in range(1, limit + 1):
            result = i * num
            # Используем f-строки с выравниванием:
            # {value:>{width}} - выравнивание по правому краю
            # {value:<{width}} - выравнивание по левому краю
            # {value:^{width}} - выравнивание по центру
            print(f"{str(num).rjust(max_num_len)} x {str(i).rjust(max_i_len)} = {str(result).rjust(max_result_len)}")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

# Для демонстрации раскомментируйте вызов:
multiplication_table_formatted_dynamic()
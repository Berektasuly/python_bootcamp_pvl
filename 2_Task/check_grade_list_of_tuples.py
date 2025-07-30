def check_grade_list_of_tuples():
    # Список кортежей: (минимальный балл, оценка).
    # Важно: должен быть отсортирован по убыванию минимального балла.
    grade_ranges = [
        (90, "Отлично"),
        (70, "Хорошо"),
        (40, "Удовлетворительно"),
        (0, "Не сдал")
    ]

    try:
        score = int(input("Введите ваш балл (от 0 до 100): "))
        if not (0 <= score <= 100):
            print("Балл должен быть от 0 до 100.")
            return

        for threshold, grade in grade_ranges:
            if score >= threshold:
                print(grade)
                return
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

# Для демонстрации раскомментируйте вызов:
check_grade_list_of_tuples()
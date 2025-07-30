def check_grade_dict():
    # Словарь, где ключ - минимальный балл для оценки, значение - сама оценка
    grades_map = {
        90: "Отлично",
        70: "Хорошо",
        40: "Удовлетворительно",
        0: "Не сдал" # Начальный порог для "Не сдал"
    }

    try:
        score = int(input("Введите ваш балл (от 0 до 100): "))
        if not (0 <= score <= 100):
            print("Балл должен быть от 0 до 100.")
            return

        # Итерируем по порогам оценок в убывающем порядке,
        # чтобы первое совпадение дало правильную оценку.
        for threshold in sorted(grades_map.keys(), reverse=True):
            if score >= threshold:
                print(grades_map[threshold])
                return
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

# Для демонстрации раскомментируйте вызов:
check_grade_dict()
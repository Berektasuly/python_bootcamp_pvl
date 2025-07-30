def multiplication_table_html():
    try:
        num = int(input("Введите число для таблицы умножения: "))
        limit = int(input("До какого числа (например, 10 или 20) вывести таблицу: "))

        if limit <= 0:
            print("Лимит должен быть положительным числом.")
            return

        html_output = f"<h2>Таблица умножения для {num}</h2>\n"
        html_output += "<table border='1' style='border-collapse: collapse; width: 20%;'>\n"
        html_output += "  <tr><th>Множитель 1</th><th>x</th><th>Множитель 2</th><th>=</th><th>Результат</th></tr>\n"

        for i in range(1, limit + 1):
            result = i * num
            html_output += f"  <tr><td>{num}</td><td>x</td><td>{i}</td><td>=</td><td>{result}</td></tr>\n"

        html_output += "</table>"

        print("\nСкопируйте следующий HTML-код и вставьте его в файл .html для просмотра:")
        print("-" * 50)
        print(html_output)
        print("-" * 50)

    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

# Для демонстрации раскомментируйте вызов:
multiplication_table_html()
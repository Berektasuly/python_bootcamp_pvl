def sum_up_to_n_loop():
    try:
        n = int(input("Введите целое число N: "))
        if n < 0:
            print("N должно быть неотрицательным числом.")
            return

        total_sum = 0
        for i in range(1, n + 1): # Цикл от 1 до N включительно
            total_sum += i
        print(f"Сумма чисел от 1 до {n} равна: {total_sum}")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")

# Для демонстрации раскомментируйте вызов:
sum_up_to_n_loop()
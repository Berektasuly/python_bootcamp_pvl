import timeit

def compare_sum_methods():
    test_n = 10**6 # Большое число для сравнения

    print(f"\nТестирование для N = {test_n}:")

    # Тестирование цикла
    loop_code = f"""
total_sum = 0
for i in range(1, {test_n}+1):
    total_sum += i
    """
    # Выполним 100 раз для получения более точных данных
    loop_time = timeit.timeit(loop_code, number=100)
    print(f"Время выполнения циклом (100 повторений): {loop_time:.6f} секунд")

    # Тестирование формулы Гаусса
    gauss_code = f"""
total_sum = {test_n} * ({test_n} + 1) // 2
    """
    # Выполним намного больше раз, т.к. очень быстро
    gauss_time = timeit.timeit(gauss_code, number=100000)
    print(f"Время выполнения формулой Гаусса (100000 повторений): {gauss_time:.6f} секунд")

    print("\nКак видите, формула Гаусса значительно быстрее, особенно для больших N.")

# Для демонстрации раскомментируйте вызов:
compare_sum_methods()
import random

def secret_game_recursive(secret, attempts=1):
    try:
        guess = int(input(f"Попытка {attempts}. Угадайте число от 1 до 10: "))
        if guess < 1 or guess > 10:
            print("Пожалуйста, введите число в диапазоне от 1 до 10.")
            return secret_game_recursive(secret, attempts) # Повторить попытку без увеличения счетчика
        elif guess < secret:
            print("Загаданное число больше!")
            return secret_game_recursive(secret, attempts + 1)
        elif guess > secret:
            print("Загаданное число меньше!")
            return secret_game_recursive(secret, attempts + 1)
        else:
            print(f"Поздравляю! Вы угадали число {secret} за {attempts} попыток.")
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")
        return secret_game_recursive(secret, attempts) # Повторить попытку без увеличения счетчика

# Пример вызова:
secret_game_recursive(random.randint(1, 10))
# Завдання 1
# Замикання в програмуванні - це функція, яка зберігає посилання на змінні зі свого лексичного контексту, тобто з області, де вона була оголошена.
# Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і повторного використання вже обчислених значень чисел Фібоначчі.


def caching_fibonacci():
    """
    Returns a function that calculates the Fibonacci sequence using caching.

    The returned function, `fibonacci`, takes an integer `n` as input and returns the `n`-th Fibonacci number.
    The function uses a cache to store previously computed Fibonacci numbers, which improves performance by avoiding redundant calculations.

    Returns:
        fibonacci (function): A function that calculates the `n`-th Fibonacci number using caching.
    """
    # Створюємо порожній словник cache для зберігання обчислених значень
    cache = {}

    # Внутрішня функція для обчислення n-го числа Фібоначчі
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        # Обчислюємо значення, якщо його немає в кеші, і зберігаємо його
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо внутрішню функцію fibonacci
    return fibonacci

# Приклад використання
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610

# Завдання 2
# Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати всі дійсні числа, що вважаються частинами доходів, 
# і повертати їх як генератор. Дійсні числа у тексті записані без помилок, чітко відокремлені пробілами з обох боків. 
# Також потрібно реалізувати функцію sum_profit, яка буде використовувати generator_numbers для підсумовування цих чисел і обчислення загального прибутку.

import re
from typing import Callable

def generator_numbers(text: str):
    """
    A generator function that extracts all the floating-point numbers from a given text.

    Args:
        text (str): The input text from which numbers need to be extracted.

    Yields:
        float: The floating-point numbers extracted from the text.

    """
    # Використовуємо регулярний вираз для знаходження всіх дійсних чисел, відокремлених пробілами
    pattern = r'(?<!\S)(\d+\.\d+|\d+)(?!\S)'
    matches = re.findall(pattern, text)
    
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable):
    # Ініціалізуємо загальний прибуток
    total_profit = 0
    
    # Використовуємо генератор для підсумовування чисел
    for number in func(text):
        total_profit += number
    
    return total_profit

# Приклад використання
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}") # Загальний дохід: 1351.46

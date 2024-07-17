# Завдання 3 (не обов'язкове)
# Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка, 
# і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. 
# Також користувач може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня

import sys
import re
from typing import List, Dict, Callable

def parse_log_line(line: str) -> Dict[str, str]:
    # Парсимо рядок логу на складові: дата, час, рівень, повідомлення
    match = re.match(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.+)', line)
    if match:
        return {
            'date': match.group(1),
            'time': match.group(2),
            'level': match.group(3),
            'message': match.group(4)
        }
    return {}

def load_logs(file_path: str) -> List[Dict[str, str]]:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parsed_line = parse_log_line(line.strip())
                if parsed_line:
                    logs.append(parsed_line)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")
    return logs

def filter_logs_by_level(logs: List[Dict[str, str]], level: str) -> List[Dict[str, str]]:
    return [log for log in logs if log['level'].lower() == level.lower()]

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    levels = ['INFO', 'ERROR', 'DEBUG', 'WARNING']
    counts = {level: 0 for level in levels}
    for log in logs:
        if log['level'] in counts:
            counts[log['level']] += 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_logfile> [log_level]")
        return

    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    if not logs:
        return

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        if filtered_logs:
            print(f"\nДеталі логів для рівня '{log_level.upper()}':")
            for log in filtered_logs:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nNo logs found for level '{log_level.upper()}'.")

if __name__ == "__main__":
    main()


# Використання скрипту:

    # Виведення статистики логів:
    # python main.py logfile.log
    

    # Фільтрація за рівнем логування:
    # python main.py logfile.log error
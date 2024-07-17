# Завдання 3 (не обов'язкове)
# Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка, 
# і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. 
# Також користувач може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня

import sys
import re
from typing import List, Dict, Callable

def parse_log_line(line: str) -> Dict[str, str]:
    """
    Parses a log line and returns a dictionary containing the parsed components.

    Args:
        line (str): The log line to be parsed.

    Returns:
        dict: A dictionary containing the parsed components of the log line.
              The dictionary has the following keys:
              - 'date': The date component of the log line.
              - 'time': The time component of the log line.
              - 'level': The level component of the log line.
              - 'message': The message component of the log line.

    """
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
    """
    Load logs from a file and return a list of dictionaries representing each log entry.

    Args:
        file_path (str): The path to the log file.

    Returns:
        List[Dict[str, str]]: A list of dictionaries representing each log entry.
    """
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
    """
    Filters a list of logs based on the specified log level.

    Args:
        logs (List[Dict[str, str]]): A list of logs, where each log is represented as a dictionary.
        level (str): The log level to filter by.

    Returns:
        List[Dict[str, str]]: A filtered list of logs that match the specified log level.
    """
    return [log for log in logs if log['level'].lower() == level.lower()]

def count_logs_by_level(logs: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Count the number of logs for each log level.

    Args:
        logs (List[Dict[str, str]]): A list of log dictionaries, where each dictionary represents a log entry.

    Returns:
        Dict[str, int]: A dictionary containing the count of logs for each log level. The keys are log levels
        (e.g., 'INFO', 'ERROR', 'DEBUG', 'WARNING') and the values are the corresponding counts.
    """
    levels = ['INFO', 'ERROR', 'DEBUG', 'WARNING']
    counts = {level: 0 for level in levels}
    for log in logs:
        if log['level'] in counts:
            counts[log['level']] += 1
    return counts

def display_log_counts(counts: Dict[str, int]):
    """
    Display the log counts for each log level.

    Args:
        counts (Dict[str, int]): A dictionary containing the log levels and their respective counts.

    Returns:
        None
    """
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")

def main():
    """
    Entry point of the program.
    
    This function takes command line arguments, loads logs from a file, counts the logs by level,
    and displays the log counts. If a log level is provided, it filters the logs by that level
    and displays the filtered logs.
    """
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
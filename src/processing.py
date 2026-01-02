from datetime import datetime
from pathlib import Path
from typing import Any, Dict

data_dir = Path(__file__).parent.parent / "data"


def filter_by_state(operations: list[dict[str, object]], state: str = "EXECUTED") -> list[dict[str, object]]:
    """Функция возвращает отсортированный список словарей."""
    sorted_dictionaries_list = []  # Список подходящих словарей
    for dictionary in operations:
        if dictionary.get("state") == state:  # Сортировка словарей по тегу 'state'
            sorted_dictionaries_list.append(dictionary)
    return sorted_dictionaries_list


def parse_date(dictionary: Dict[str | Any]) -> datetime:
    """Функция для парсинга даты"""
    date_str = dictionary.get("date")  # Получение даты из словаря в списке
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")


def sort_by_date(dictionaries_list: list[Dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция для сортировки списка по дате"""
    return sorted(dictionaries_list, key=parse_date, reverse=reverse)

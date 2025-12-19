from datetime import datetime
from typing import Any, Dict

MIN_DATE = datetime.min  # Минимально возможная дата
dictionaries_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]  # Пример ввода списка словарей


def filter_by_state(dictionaries_list: list[dict[str, object]], state: str = "EXECUTED") -> list[dict[str, object]]:
    """Функция возвращает отсортированный список словарей."""
    sorted_dictionaries_list = []  # Список подходящих словарей
    for dictionary in dictionaries_list:
        if dictionary.get("state") == state:  # Сортировка словарей по тегу 'state'
            sorted_dictionaries_list.append(dictionary)
    return sorted_dictionaries_list


def parse_date(dictionary: Dict[str, Any]) -> datetime:
    """Функция для парсинга даты"""
    date_str = dictionary.get("date")  # Получение даты из словаря в списке
    if date_str:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    return MIN_DATE


def sort_by_date(dictionaries_list: list[Dict[str, Any]], reverse: bool = True) -> list[dict[str, Any]]:
    """Функция для сортировки списка по дате"""
    return sorted(dictionaries_list, key=parse_date, reverse=reverse)

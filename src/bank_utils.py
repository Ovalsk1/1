import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция фильтрует список банковских операций, оставляя только те, в описании которых содержится заданная строка.
    Поиск основан на регулярных выражениях (регэкспах).

    :param data: список словарей с банковскими операциями
    :param search: строка для поиска в описаниях операций
    :return: список словарей, содержащих совпадающие операции
    """
    pattern = re.compile(search, re.IGNORECASE)  # Создаём регулярное выражение с игнорированием регистра
    result = []

    for entry in data:
        description = entry.get("description", "")
        if pattern.search(description):
            result.append(entry)

    return result


def count_bank_operations(data: list[dict], categories: list[str]) -> dict[str, int]:
    """
    Функция принимает список банковских операций и список категорий операций,
    и возвращает словарь, где ключами являются категории, а значениями -
    количество операций, относящихся к каждой категории.

    Категории определяются по наличию в описании операции (поле description).

    :param data: список словарей с операциями банка
    :param categories: список категорий операций
    :return: словарь с количеством операций в каждой категории
    """
    counter = Counter()

    for operation in data:
        description = operation.get("description", "").strip().lower()  # Приведение описания к единому регистру
        for category in categories:
            if category.lower() in description:
                counter[category] += 1  # Увеличиваем счётчик операций в данной категории
                break  # Одна операция может относиться только к одной категории

    return dict(counter)

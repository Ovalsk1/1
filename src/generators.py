from pathlib import Path
from typing import Any, Generator

data_dir = Path(__file__).parent.parent / "data"


def filter_by_currency(
    transactions: list[dict[str, Any]], currency: str = "RUB"
) -> Generator[dict[str, dict[str, Any]], Any, None]:
    """
    Функция принимает список транзакций и возвращает итератор выдающий транзакции по заданой валюте
    """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        curr = operation_amount.get("currency", {}).get("code")
        if curr == currency:
            yield transaction


def filter_by_currency_not_json(
    transactions: list[dict[str, Any]], currency: str = "RUB"
) -> Generator[dict[str, dict[str, Any]], Any, None]:
    """
    Функция принимает список транзакций и возвращает итератор выдающий транзакции по заданой валюте.
    Предназначена НЕ для ".json" файлов
    """
    for transaction in transactions:
        curr = transaction.get("currency_code")
        if curr == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Generator[dict[str, Any] | None]:
    """
    Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    for text in transactions:
        yield text.get("description")


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
    """Генератор, выдающий номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for i in range(start, end + 1):
        card_number = f"{i:016d}"
        formatted_number = " ".join(card_number[i:i + 4] for i in range(0, 16, 4))
        yield formatted_number

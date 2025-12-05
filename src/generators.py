from typing import Any, Generator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(
    transactions: list[dict[str, Any]], currency: str = "USD"
) -> Generator[dict[str, dict[str, Any]], Any, None]:
    """
    Функция принимает список транзакций и возвращает итератор выдающий транзакции по заданой валюте
    """
    for transaction in transactions:
        operation_amount = transaction.get("operationAmount", {})
        curr = operation_amount.get("currency", {}).get("code")
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
        formatted_number = " ".join(card_number[i : i + 4] for i in range(0, 16, 4))
        yield formatted_number

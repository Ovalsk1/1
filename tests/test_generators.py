from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


def test_filter_by_currency() -> None:
    """ Тест функции 'filter_by_currency'"""
    usd_trans = filter_by_currency(transactions, currency="USD")
    assert len(list(usd_trans)) == 3
    assert all(text["operationAmount"]["currency"]["code"] == "USD" for text in usd_trans)
    rub_trans = filter_by_currency(transactions, currency="RUB")
    assert len(list(rub_trans)) == 2
    assert all(text["operationAmount"]["currency"]["code"] == "RUB" for text in rub_trans)


def test_transaction_descriptions() -> None:
    """Тест функции 'transaction_descriptions'"""
    result = list(transaction_descriptions(transactions))
    assert len(result) == 5
    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации",
    ]


def test_card_number_generator() -> None:
    """Тест функции 'card_number_generator'"""
    result = list(card_number_generator(1, 5))
    assert len(result) == 5
    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]

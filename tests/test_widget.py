import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "parameter, expected_result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(parameter: str, expected_result: str) -> None:
    """Функция тестирующая работу функции 'mask_account_card' в модуле 'widget'"""
    result = mask_account_card(parameter)
    assert result == expected_result


def test_get_date() -> None:
    """Тест проверяет корректность преобразования даты из ISO-формата в модуле 'widget' в формат DD.MM.YYYY"""
    result = get_date("2024-03-11T02:26:18.671407")
    assert result == "11.03.2024"

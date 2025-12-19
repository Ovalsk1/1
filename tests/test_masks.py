import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def test_parameter_get_mask_card_number() -> int:
    """Фикстура для теста функции 'get_mask_card_number' в модуле 'masks'"""
    return 1234567890123456


@pytest.fixture
def test_parameter_get_mask_account() -> int:
    """Фикстура для теста функции 'get_mask_account' в модуле 'masks'"""
    return 123456


def test_get_mask_card_number(test_parameter_get_mask_card_number: int) -> None:
    """Функция тестирования маскировки номера карты"""
    result = get_mask_card_number(test_parameter_get_mask_card_number)
    assert result == "1234 56** **** 3456"


def test_get_mask_account(test_parameter_get_mask_account: int) -> None:
    """Функция тестирования маскировки номера счета"""
    result = get_mask_account(test_parameter_get_mask_account)
    assert result == "**3456"

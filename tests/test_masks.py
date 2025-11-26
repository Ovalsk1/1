import pytest


@pytest.fixture
def get_mask_card_number() -> str:
    return "1234 56** **** 3456"


@pytest.fixture
def get_mask_account() -> str:
    return "**3456"


def test_get_mask_card_number(get_mask_card_number:int) -> None:
    assert get_mask_card_number == "1234 56** **** 3456"


def test_get_mask_account(get_mask_account:int) -> None:
    assert get_mask_account == "**3456"

import pytest
from src.widget import get_date, mask_account_card

@pytest.mark.parametrize("mask_account_card",("Visa Platinum 7000 79** **** 6361", "Maestro 7000 79** **** 6361", "Счет **4305"))

def test_mask_account_card(mask_account_card: str) -> None:
    assert mask_account_card
    assert mask_account_card
    assert mask_account_card


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"

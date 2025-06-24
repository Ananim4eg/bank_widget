import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture()
def my_card_number() -> str:
    return "7000792289606361"


@pytest.fixture()
def my_account_number() -> str:
    return "73654108430135874305"


def test_mask_card(my_card_number: str) -> None:
    assert get_mask_card_number(my_card_number) == "7000 79** **** 6361"


def test_mask_account(my_account_number: str) -> None:
    assert get_mask_account(my_account_number) == "**4305"

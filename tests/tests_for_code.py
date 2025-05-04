import pytest

from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date


@pytest.fixture()
def my_card_number():
    return 7000792289606361


@pytest.fixture()
def my_account_number():
    return 73654108430135874305


def test_mask_card(my_card_number):
    assert get_mask_card_number(my_card_number) == "7000 79** **** 6361"


def test_mask_account(my_account_number):
    assert  get_mask_account(my_account_number) == "**4305"


@pytest.mark.parametrize("my_string, result_of_masking", [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Счет 35383033474447895560", "Счет **5560"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Что-то 73654108430135874305", "Неверный формат, введенных, данных"),
    ("Что-то 8990922113665229", "Неверный формат, введенных, данных"),
    ("Счет счет 73654108430", "Неверный формат, введенных, данных"),
    ("Что-то 73654108430135874305", "Неверный формат, введенных, данных"),
    ("", "Неверный формат, введенных, данных"),
    ("Что-то 899пв113665229", "Неверный формат, введенных, данных"),
    ("Что-то 899d113665229", "Неверный формат, введенных, данных"),
    ("WTF 35383033474447895560", "Неверный формат, введенных, данных"),
    ("Счет35383033474447895560", "Неверный формат, введенных, данных"),
    ("WTF 35383033474447895560", "Неверный формат, введенных, данных"),

])
def test_mask_account_card(my_string, result_of_masking):
    assert mask_account_card(my_string) == result_of_masking


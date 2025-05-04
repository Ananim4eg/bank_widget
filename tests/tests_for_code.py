from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date


def test_mask_card():
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"


def test_mask_account():
    assert  get_mask_account(73654108430135874305) == "**4305"


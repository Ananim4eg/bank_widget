from typing import List, Union, Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture()
def my_transactions() -> List[dict]:
    return [
        {
            "id": 939719570,
            "state": "expected",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "expected",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 153764598,
            "state": "expected",
            "date": "2017-12-05T21:20:15.184932",
            "operationAmount": {"amount": "4563.56", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод организации",
            "from": "Счет 64686473678894779589",
            "to": "Счет 75651664879060286425",
        },
        {
            "id": 427386633,
            "state": "expected",
            "date": "2019-06-12T15:22:13.143563",
            "operationAmount": {"amount": "34385.12", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 73654108430135874305",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 155498340,
            "state": "expected",
            "date": "2020-01-03T04:23:45.216345",
            "operationAmount": {"amount": "2500.00", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод с карты на карту",
            "from": "MasterCard 7158300734726758",
            "to": "Visa Classic 6831982476737658",
        },
        {
            "id": 843957626,
            "state": "expected",
            "date": "2019-02-02T12:20:34.543163",
            "operationAmount": {"amount": "345.16", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Gold 5999414228426353",
            "to": "Visa Platinum 8990922113665229",
        },
    ]


def test_filter_by_currency(my_transactions: List[dict]) -> None:
    assert list(filter_by_currency(my_transactions, "RUB"))[0] == {
        "id": 155498340,
        "state": "expected",
        "date": "2020-01-03T04:23:45.216345",
        "operationAmount": {"amount": "2500.00", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод с карты на карту",
        "from": "MasterCard 7158300734726758",
        "to": "Visa Classic 6831982476737658",
    }

    assert list(filter_by_currency(my_transactions, "CNY")) == []

    assert list(filter_by_currency([], "CNY")) == []

    assert list(filter_by_currency(my_transactions, " ")) == []

    assert list(filter_by_currency([], " ")) == []


expected = [
    [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод с карты на карту",
    ],
    [],
]


@pytest.mark.parametrize(
    "my_transactions, expected",
    [
        (
            my_transactions,
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод с карты на карту",
            ],
        )
    ],
    indirect=["my_transactions"],
)
def test_transaction_descriptions(my_transactions: Any, expected: list) -> None:
    assert list(transaction_descriptions(my_transactions)) == expected

    assert list(transaction_descriptions([])) == []

    assert list(transaction_descriptions(list(my_transactions)[1:4])) == expected[1:4]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            10,
            15,
            [
                "0000 0000 0000 0010",
                "0000 0000 0000 0011",
                "0000 0000 0000 0012",
                "0000 0000 0000 0013",
                "0000 0000 0000 0014",
                "0000 0000 0000 0015",
            ],
        ),
        (
            0,
            5,
            [
                "0000 0000 0000 0000",
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9999999999999995,
            9999999999999999,
            [
                "9999 9999 9999 9995",
                "9999 9999 9999 9996",
                "9999 9999 9999 9997",
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
        (15, 10, []),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: Union[list, str]) -> None:
    assert list(card_number_generator(start, stop)) == expected

    assert next(card_number_generator(-5, 6)) == "Некорректные диапазоны"

    assert next(card_number_generator(9999999999999995, 99999999999999999)) == "Некорректные диапазоны"

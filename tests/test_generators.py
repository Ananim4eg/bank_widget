import pytest

from src.generators import card_number_generator, transaction_descriptions, filter_by_currency

@pytest.fixture()
def my_transactions() -> list:
    return \
        [
        {
              "id": 939719570,
              "state": "EXECUTED",
              "date": "2018-06-30T02:08:58.425572",
              "operationAmount": {
                  "amount": "9824.07",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод организации",
              "from": "Счет 75106830613657916952",
              "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 153764598,
            "state": "EXECUTED",
            "date": "2017-12-05T21:20:15.184932",
            "operationAmount": {
                "amount": "4563.56",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 64686473678894779589",
            "to": "Счет 75651664879060286425"
        },
        {
            "id": 427386633,
            "state": "EXECUTED",
            "date": "2019-06-12T15:22:13.143563",
            "operationAmount": {
                "amount": "34385.12",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 73654108430135874305",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 155498340,
            "state": "EXECUTED",
            "date": "2020-01-03T04:23:45.216345",
            "operationAmount": {
                "amount": "2500.00",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 7158300734726758",
            "to": "Visa Classic 6831982476737658"
        },
        {
            "id": 843957626,
            "state": "EXECUTED",
            "date": "2019-02-02T12:20:34.543163",
            "operationAmount": {
                "amount": "345.16",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод с карты на кару",
            "from": "Visa Gold 5999414228426353",
            "to": "Visa Platinum 8990922113665229"
        }
    ]


def test_filter_by_currency(my_transactions):
    assert  list(filter_by_currency(my_transactions, "RUB"))[0] == {
            "id": 155498340,
            "state": "EXECUTED",
            "date": "2020-01-03T04:23:45.216345",
            "operationAmount": {
                "amount": "2500.00",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 7158300734726758",
            "to": "Visa Classic 6831982476737658"
        }

    assert list(filter_by_currency(my_transactions, "CNY")) == []

    assert list(filter_by_currency([], "CNY")) == []

    assert list(filter_by_currency(my_transactions, " ")) == []

    assert list(filter_by_currency([], " ")) == []


# @pytest.mark.parametrize("my_list, executed", [my_transactions, ])
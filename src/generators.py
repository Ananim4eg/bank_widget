from typing import Iterable, List

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(my_list: List[dict], my_currency: str) -> Iterable:
    """Возвращает итератор, содержащий словари с информацией о транзакциях, выбранных по заданному параметру"""
    return (trans for trans in my_list if trans["operationAmount"]["currency"]["code"] == my_currency)


def transaction_descriptions(my_list: List[dict]) -> Iterable:
    """Возвращает описание транзакции. Например:'Перевод с карты на карту'"""
    new_gen = [trans["description"] for trans in my_list]
    for i in new_gen:
        yield i


def card_number_generator(start: int, stop: int) -> Iterable:
    """Возвращает номера карт, формирующиеся в диапазоне заданных значений"""
    try:
        if (start < 0 or stop < 0) or (start > 9999999999999999 or stop > 9999999999999999):
            raise StopIteration("Error__")
        pattern = 10000000000000000
        for i in range(start, stop + 1):
            number_card = str(pattern + i)[1:]
            yield f"{number_card[:4]} {number_card[4:8]} {number_card[8:12]} {number_card[12:]}"
    except StopIteration:
        yield "Некорректные диапазоны"

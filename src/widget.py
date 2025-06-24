import re
from datetime import datetime
from types import NoneType

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """Функция маскирующая номера карты или счета"""
    supported_cards = [
        "visa gold",
        "visa platinum",
        "visa classic",
        "mastercard",
        "maestro",
        "discover",
        "american express",
        "visa",
        "мир",
    ]

    # Проверяем что во введенной строке есть символы и есть хотя бы 1 пробел
    if (
        type(card_or_account_info) in [float, NoneType]
        or not len(card_or_account_info)
        or " " not in card_or_account_info
    ):
        return "Неверный формат, введенных, данных"

    card_or_account_list = card_or_account_info.rsplit(maxsplit=1)

    try:
        # Проверяем что номер счет или кары состоит из цифр
        if int(card_or_account_list[1]):
            # Проверяем что введенная строка не имеет в себе слово "счет" и длина номера равна 16 цифрам
            if len(card_or_account_list[1]) == 16 and card_or_account_list[0].lower() in supported_cards:
                return f"{card_or_account_list[0]} {get_mask_card_number(card_or_account_list[1])}"
            # Проверяем что введенная строка имеет в себе слово "счет" и длина номера равна 20 цифрам
            elif len(card_or_account_list[1]) == 20 and card_or_account_list[0].lower() == "счет":
                return f"{card_or_account_list[0]} {get_mask_account(card_or_account_list[1])}"
            else:
                return "Неверный формат, введенных, данных"

    except ValueError:
        return "Неверный формат, введенных, данных"
    else:
        return "Неверный формат, введенных, данных"


def get_date(date: str) -> str:
    """Приводит строку с датой к формату 'ДД.ММ.ГГГГ'"""

    pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}"

    try:
        if re.fullmatch(pattern, date):
            format_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            format_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ")
        return format_date.strftime("%d.%m.%Y")

    except ValueError:
        return "Дата должна быть введена в формате <ГГГГ-ММ-ДДTЧЧ:мм:СС.сссссс>"

    except TypeError:
        return "Дата должна быть введена в формате <ГГГГ-ММ-ДДTЧЧ:мм:СС.сссссс>"

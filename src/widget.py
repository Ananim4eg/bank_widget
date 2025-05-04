from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """Функция маскирующая номера карты или счета"""
    card_or_account_list = card_or_account_info.rsplit(maxsplit=1)
    # Проверяем что номер счет или кары состоит из цифр
    if int(card_or_account_list[1]):
        # Проверяем что введенная строка не имеет в себе слово "счет" и длина номера равна 16 цифрам
        if len(card_or_account_list[1]) == 16 and "счет" not in card_or_account_info.lower():
            return f"{card_or_account_list[0]} {get_mask_card_number(int(card_or_account_list[1]))}"
        # Проверяем что введенная строка имеет в себе слово "счет" и длина номера равна 20 цифрам
        elif len(card_or_account_list[1]) == 20 and "счет" in card_or_account_info.lower():
            return f"{card_or_account_list[0]} {get_mask_account(int(card_or_account_list[1]))}"
        else:
            return "Неверный формат, введенных, данных"
    else:
        return "Неверный формат, введенных, данных"


def get_date(date: str) -> str:
    """Приводит строку с датой к формату 'ДД.ММ.ГГГГ'"""
    format_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")

    return format_date.strftime("%d.%m.%Y")

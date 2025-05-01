from datetime import datetime

import masks



def mask_account_card(card_or_account_info: str) -> str:
    """Функция маскирующая номера карты или счета"""
    card_or_account_list = card_or_account_info.rsplit(maxsplit=1)
    
    if len(card_or_account_list[1]) == 16:
        return card_or_account_list[0] + " " + masks.get_mask_card_number(int(card_or_account_list[1]))
    else:
        return card_or_account_list[0] + " " + masks.get_mask_account(int(card_or_account_list[1]))


def get_date(date: str) -> str:
    """Приводит строку с датой к формату 'ДД.ММ.ГГГГ'"""
    format_date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")

    return format_date.strftime("%d.%m.%Y")


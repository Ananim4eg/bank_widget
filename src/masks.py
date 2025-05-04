def get_mask_card_number(number_card: int) -> str:
    """Маскирует номер карты"""
    if len(str(number_card)) == 16:
        return f"{str(number_card)[:4]} {str(number_card)[4:6]}** **** {str(number_card)[-4:]}"
    else:
        return "Неверный формат, введенных, данных"


def get_mask_account(number_account: int) -> str:
    """Маскирует номер счета"""
    if len(str(number_account)) == 20:
        return f"**{str(number_account)[-4:]}"
    else:
        return "Неверный формат, введенных, данных"
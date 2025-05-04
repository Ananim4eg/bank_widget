def get_mask_card_number(number_card: int) -> str:
    """Маскирует номер карты"""

    return f"{str(number_card)[:4]} {str(number_card)[4:6]}** **** {str(number_card)[-4:]}"


def get_mask_account(number_account: int) -> str:
    """Маскирует номер счета"""

    return f"**{str(number_account)[-4:]}"

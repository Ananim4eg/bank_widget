import masks


def mask_account_card(card_or_account_info: str) -> str:
    
    card_or_account_list = card_or_account_info.rsplit(maxsplit=1)
    
    if len(card_or_account_list[1]) == 16:
        return card_or_account_list[0] + " " + masks.get_mask_card_number(int(card_or_account_list[1]))
    else:
        return card_or_account_list[0] + " " + masks.get_mask_account(int(card_or_account_list[1]))


print(mask_account_card('Visa Platinum 8990922113665229'))

    
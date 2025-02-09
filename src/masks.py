def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return "Номер карты введён не корректно"


# print(get_mask_card_number("7000792289606361"))


def get_mask_account(mask_account: str) -> str:
    """Функция маскировки номера банковского счета"""
    if len(mask_account) == 20 and mask_account.isdigit():
        return f"**{mask_account[16:]}"
    return "Номер счёта введён не корректно"


# print(get_mask_account("73654108430135874305"))

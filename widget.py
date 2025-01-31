from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_type_card_num: str) -> str:
    """ Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    account_type_card_num_list = account_type_card_num.split(" ")
    if len(account_type_card_num_list[-1]) < 20 and len(account_type_card_num) > 16:
        mask_card_number = get_mask_card_number(account_type_card_num_list[-1])
        account_type_card_num_list[-1] = mask_card_number
        if mask_card_number == "Некорректный ввод":
            return "Некорректный ввод данных"
        return " ".join(account_type_card_num_list)
    if len(account_type_card_num_list[-1]) == 20 and len(account_type_card_num) == 25:
        mask_account = get_mask_account(account_type_card_num_list[-1])
        account_type_card_num_list[-1] = mask_account
        return " ".join(account_type_card_num_list)
    return "Некорректный ввод данных"


print(mask_account_card("Visa Platinum 7000792289606361"))
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("Счёт 12345123451234512345"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))


from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_type_card_num: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
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


def get_date(type_time: str) -> str:
    """Функция, которая возвращает строку с датой в формате
    "ДД.ММ.ГГГГ" """
    if len(type_time) != 26:
        return "Некорректный ввод"
    return f"{type_time[8:10]}.{type_time[5:7]}.{type_time[0:4]}"

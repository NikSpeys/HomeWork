def filter_by_currency(my_dict: list[dict], currency_code: str = 'USD') -> str:
    """функция, которая принимает список словарей, представляющих транзакции и
    возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    if not my_dict:
        return 'Список транзакций пуст'
    if currency_code not in ['USD']:
        return 'Код валюты не найден'
    for transaction in my_dict:
        if transaction['operationAmount']['currency']['code'] == currency_code:
            yield transaction

    return iter([])


def transaction_descriptions(my_dict: list[dict]) -> list:
    """Функция, которая принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    result = (i.get('description') for i in my_dict)
    for x in result:
        yield x

    return iter([])


def card_number_generator(start: int, stop: int) -> str:
    """Функция, которая генерирует номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999"""
    for number in range(start, stop + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formated_card_number = f'{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}'
        yield formated_card_number

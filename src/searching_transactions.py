import re
from collections import Counter


def search_transaction(transactions: list[dict], search_string: str) -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка
    """
    if not search_string:
        return transactions

    pattern = re.compile(search_string, re.IGNORECASE)
    operations_filter = []
    for transaction in transactions:
        if "description" in transaction and re.search(pattern, transaction["description"]):
            operations_filter.append(transaction)

    return operations_filter


def count_description(transactions: list[dict], categories: list[str]) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи - это названия категорий
    """
    categories_dict = []
    for transaction in transactions:
        descript = transaction["description"]
        for category in categories:
            if re.search(category, descript, re.IGNORECASE):
                categories_dict.append(category)
    counter_descriptions = Counter(categories_dict)
    return counter_descriptions
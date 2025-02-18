def filter_by_state(data_list: list, state: str = "EXECUTED") -> list:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ "state"
    соответствует указанному значению.
    """
    filter_item = []
    for item in data_list:
        if item.get("state") == state:
            filter_item.append(item)
    return filter_item


def sort_by_date(date: list, reverse: bool = True) -> list:
    """Функция возвращает отсортированный список по дате"""
    sorted_list = sorted(date, key=lambda x: x.get("date"), reverse=reverse)
    return sorted_list

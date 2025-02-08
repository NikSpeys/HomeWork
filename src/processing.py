def filter_by_state(date: list[dict[str, any]], state: str = "EXECUTED") -> list[dict[str, any]]:
    # executed_items = list(dict(filter(filter_by_state(state))))
    filtered_list = list(filter(lambda x: x["state"] == "EXECUTED", date))
    return filtered_list


print(filter_by_state(
    [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
     {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
     {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
     {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]))


def sort_by_date(date: list[dict[str, any]], reverse: bool = True) -> list[dict[str, any]]:
    pass
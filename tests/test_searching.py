from collections import Counter

import pytest

from src.searching_transactions import search_transaction, count_description


@pytest.fixture
def tran_list():
    return [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560",
        },
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
    ]


@pytest.fixture
def descript_dict():
    return [
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {"name": "руб.", "code": "RUB"},
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        }
    ]


def test_operations_search(tran_list, descript_dict):
    assert search_transaction(tran_list, "Открытие вклада") == descript_dict


@pytest.fixture
def count_descript_dict():
    return Counter({"Перевод организации": 1, "Открытие вклада": 1})


def test_count_description(tran_list, count_descript_dict):
    assert (count_description(tran_list, ["Перевод организации", "Открытие вклада"]) == count_descript_dict)
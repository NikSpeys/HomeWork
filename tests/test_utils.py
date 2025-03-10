import os
from unittest.mock import mock_open, patch

import pytest

from src.utils import load_transactions_from_json, transaction_amount


@pytest.fixture
def path():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    return PATH_TO_FILE


@pytest.fixture
def path_empty_list():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations1.json")
    return PATH_TO_FILE


@pytest.fixture
def path_mistake_json():
    PATH_TO_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations2.json")
    return PATH_TO_FILE


def test_transactions_nofile():
    assert load_transactions_from_json("nofile") == []


def test_load_transactions(path):
    transactions = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    assert len(transactions) > 0, "Список транзакций пуст!"
    assert transactions[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_load_transactions_empty_list(path_empty_list):
    assert load_transactions_from_json(path_empty_list) == []


def test_load_transactions_mistake_json(path_mistake_json):
    assert load_transactions_from_json(path_mistake_json) == []


def test_load_transactions_from_json_with_invalid_json():
    with patch("builtins.open", mock_open(read_data="invalid_json")):
        result = load_transactions_from_json("dummy_path.json")
        assert result == []


def test_load_transactions_from_json_with_non_existent_file():
    result = load_transactions_from_json("non_existent_file.json")
    assert result == []


@pytest.fixture
def sample_transaction():
    return {"operationAmount": {"amount": 100, "currency": {"code": "USD"}}}


@pytest.fixture
def mock_get_amount():
    with patch("src.external_api.get_amount") as mock:
        yield mock


def test_transaction_amount_with_same_currency(sample_transaction):
    sample_transaction["operationAmount"]["currency"]["code"] = "RUB"
    amount = transaction_amount(sample_transaction)
    assert amount == 100

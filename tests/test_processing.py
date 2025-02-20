import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import list_of_dict_sort_res_true, list_of_dict_sorted_1, list_of_dict_sorted_2


@pytest.fixture
def list_of_dict_fixture() -> list:
    return [
        {"id": 414288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dict_ident_dates_fixture() -> list:
    return [
        {"id": 888288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def list_of_dict_ident_dates_sort():
    return [
        {"id": 888288291, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_basic(list_of_dict_fixture: list) -> None:
    assert filter_by_state(list_of_dict_fixture) == list_of_dict_sorted_1


def test_filter_by_state_with_state_arg_canceled(list_of_dict_fixture: list) -> None:
    assert filter_by_state(list_of_dict_fixture, state="CANCELED") == list_of_dict_sorted_2


def test_sort_by_date_basic(list_of_dict_fixture: list) -> None:
    assert sort_by_date(list_of_dict_fixture) == list_of_dict_sort_res_true


def test_sort_by_date_ident_dates(list_of_dict_ident_dates_fixture, list_of_dict_ident_dates_sort) -> None:
    assert sort_by_date(list_of_dict_ident_dates_fixture) == list_of_dict_ident_dates_sort

import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    """Тест проверки работы функции маскировки номера банковских карт"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    assert get_mask_card_number("9012932890606361") == "9012 93** **** 6361"
    assert get_mask_card_number("1203142289606361") == "1203 14** **** 6361"
    with pytest.raises(ValueError):
        # get_mask_card_number("5413242214")
        # get_mask_card_number("1201d")
        get_mask_card_number("12010324292390239022")
        # get_mask_card_number("")


def test_get_mask_account():
    """Тест проверки работы функции маскировки номера банковского счёта"""
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account("73654108430135874303") == "**4303"
    assert get_mask_account("73654108430135874301") == "**4301"
    with pytest.raises(ValueError):
        # get_mask_account("99992.9dfgddg92")
        # get_mask_account("999929921203901230102301203")
        get_mask_account("")
        # get_mask_account("1201d")

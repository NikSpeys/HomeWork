import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number():
    """Тест проверки работы функции маскировки номера банковских карт"""
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"
    with pytest.raises(ValueError):
        get_mask_card_number("5413242214")
    with pytest.raises(ValueError):
        get_mask_card_number("1201d")
    with pytest.raises(ValueError):
        get_mask_card_number("12010324292390239022")
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_account():
    """Тест проверки работы функции маскировки номера банковского счёта"""
    assert get_mask_account("73654108430135874305") == "**4305"
    with pytest.raises(ValueError):
        get_mask_account("99992.9dfgddg92")
    with pytest.raises(ValueError):
        get_mask_account("999929921203901230102301203")
    with pytest.raises(ValueError):
        get_mask_account("")
    with pytest.raises(ValueError):
        get_mask_account("1201d")

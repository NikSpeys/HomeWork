import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa 1234561234563456", "Visa 1234 56** **** 3456"),
        ("MasterCard 5123456789012345", "MasterCard 5123 45** **** 2345"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(value, expected) -> None:
    assert mask_account_card(value) == expected

    with pytest.raises(ValueError):
        mask_account_card("Счет 7365410843013587430")
    with pytest.raises(ValueError):
        mask_account_card("Visa abcdefgh1234567890")
    with pytest.raises(ValueError):
        mask_account_card("Счет abcdefgh1234567890")


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2023-12-25T10:00:00.000000") == "25.12.2023"


def test_get_basic() -> None:
    assert get_date("2018-10-14T08:21:33.419441") == "14.10.2018"


@pytest.mark.parametrize(
    "value, expected",
    [
        ("08:21:33.419441", "Некорректный ввод"),
        ("2018-14T08:21:33.419441", "Некорректный ввод"),
    ],
)
def test_get_date_uncorrectly(value, expected) -> None:
    assert get_date(value) == expected

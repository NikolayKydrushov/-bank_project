import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "line_being, output_string",
    [
        (7000792289606361, "7000 79** **** 6361"),
        ("7000792289606360", "7000 79** **** 6360"),
        (2, "Длина номера карты неправильна"),
        ("Длинаномеракарты", "Длина номера карты неправильна"),
    ],
)
def test_get_mask_card_number(line_being, output_string):
    assert get_mask_card_number(line_being) == output_string


@pytest.mark.parametrize(
    "line_being, output_string",
    [
        (73654108430135874305, "**4305"),
        ("73654108430135874305", "**4305"),
        (2, "Длина номера карты неправильна"),
        ("Длинаномеракарты", "Длина номера карты неправильна"),
    ],
)
def test_get_mask_account(line_being, output_string):
    assert get_mask_account(line_being) == output_string

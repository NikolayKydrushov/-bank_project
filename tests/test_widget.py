import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "line_being, output_string",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("", "Длина номера карты неправильна"),
    ],
)
def test_mask_account_card(line_being, output_string):
    assert mask_account_card(line_being) == output_string


def test_get_dat():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("") == "Длина номера карты неправильна"

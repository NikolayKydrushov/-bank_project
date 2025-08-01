import pytest

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card


def test_get_mask_card_number():
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"
    assert get_mask_card_number("7000792289606360") == "7000 79** **** 6360"
    assert get_mask_card_number(2) == "Длина номера карты неправильна"
    assert get_mask_card_number("Длинаномеракарты") == "Длина номера карты неправильна"


def test_get_mask_account():
    assert get_mask_account(73654108430135874305) == "**4305"
    assert get_mask_account("73654108430135874305") == "**4305"
    assert get_mask_account(2) == "Длина номера карты неправильна"
    assert get_mask_account("Длинаномеракарты") == "Длина номера карты неправильна"


def test_mask_account_card():
    assert (
        mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    )
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("") == "Длина номера карты неправильна"


def test_get_dat():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("") == "Длина номера карты неправильна"


list_ = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def first_test_filter_by_state(executed_list_result):
    assert filter_by_state(list_, "EXECUTED") == executed_list_result
    assert filter_by_state([], "EXECUTED") == []
    assert filter_by_state([], "") == []


def second_test_filter_by_state(canceled_list_result):
    assert filter_by_state(list_, "CANCELED") == canceled_list_result


def test_sort_by_date(list_result):
    assert sort_by_date(list_, True) == list_result

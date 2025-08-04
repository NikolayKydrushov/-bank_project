from src.processing import filter_by_state, sort_by_date

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

from src.processing import filter_by_state, sort_by_date, process_bank_search, process_bank_operations


full_list = [
        {
            "id": 464419177, "state": "CANCELED", "date": "2018-07-15T18:44:13.346362",
            "operationAmount": { "amount": "71024.64", "currency": {"name": "руб.", "code": "RUB"} },
            "description": "Перевод с карты на счет", "from": "Visa Gold 9657499677062945", "to": "Счет 19213886662094884261"
        },
        {
            "id": 560813069, "state": "CANCELED", "date": "2019-12-03T04:27:03.427014",
            "operationAmount": { "amount": "17628.50", "currency": {"name": "USD","code": "USD"} },
            "description": "Перевод организации", "from": "MasterCard 1796816785869527", "to": "Visa Classic 7699855375169288"
        },
        {
            "id": 894961746, "state": "EXECUTED", "date": "2019-08-04T20:17:25.443322",
            "operationAmount": { "amount": "2523.44", "currency": {"name": "руб.", "code": "RUB"} },
            "description": "Перевод с карты на счет", "from": "Счет 33721541831646393763", "to": "Счет 68774571780974952778"
        },
        {
            "id": 360577236, "state": "EXECUTED", "date": "2019-09-07T07:20:13.889610",
            "operationAmount": { "amount": "18536.73", "currency": {"name": "руб.","code": "RUB"} },
            "description": "Перевод с карты на карту", "from": "Maestro 4284341727554246", "to": "МИР 1582474475547301"
        }
    ]


def test_filter_by_state(executed_list_result, canceled_list_result):
    assert filter_by_state(full_list, "EXECUTED") == executed_list_result
    assert filter_by_state([], "EXECUTED") == []
    assert filter_by_state([], "") == []
    assert filter_by_state(full_list, "CANCELED") == canceled_list_result
    assert filter_by_state([], "CANCELED") == []
    assert filter_by_state([], "CAN") == []


def test_sort_by_date(list_result_ascending, list_result_descending):
    assert sort_by_date(full_list, False) == list_result_ascending
    assert sort_by_date(full_list, True) == list_result_descending
    assert sort_by_date([], False) == []
    assert sort_by_date([], True) == []


def test_process_bank_search(executed_list_result_0):
    assert process_bank_search(full_list, "Перевод с карты на счет") == executed_list_result_0
    assert process_bank_search([], "Перевод с карты на счет") == []
    assert process_bank_search([], "") == []


def test_process_bank_operations():
    assert process_bank_operations(full_list, ["Перевод с карты на счет"]) == {"Перевод с карты на счет" : 2}
    assert process_bank_operations([], ["Перевод с карты на счет"]) == {}



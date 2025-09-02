import pytest


@pytest.fixture
def list_result_ascending():
    return [
        {"id": 464419177, "state": "CANCELED", "date": "2018-07-15T18:44:13.346362",
         "operationAmount": {"amount": "71024.64", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод с карты на счет", "from": "Visa Gold 9657499677062945",
         "to": "Счет 19213886662094884261"},
        {"id": 894961746, "state": "EXECUTED", "date": "2019-08-04T20:17:25.443322",
         "operationAmount": {"amount": "2523.44", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод с карты на счет", "from": "Счет 33721541831646393763",
         "to": "Счет 68774571780974952778"},
        {"id": 360577236, "state": "EXECUTED", "date": "2019-09-07T07:20:13.889610",
         "operationAmount": {"amount": "18536.73", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод с карты на карту", "from": "Maestro 4284341727554246", "to": "МИР 1582474475547301"},
        {"id": 560813069, "state": "CANCELED", "date": "2019-12-03T04:27:03.427014",
         "operationAmount": {"amount": "17628.50", "currency": {"name": "USD", "code": "USD"}},
         "description": "Перевод организации", "from": "MasterCard 1796816785869527",
         "to": "Visa Classic 7699855375169288"}

    ]

@pytest.fixture
def list_result_descending():
    return [
        {"id": 560813069, "state": "CANCELED", "date": "2019-12-03T04:27:03.427014",
         "operationAmount": {"amount": "17628.50", "currency": {"name": "USD", "code": "USD"}},
         "description": "Перевод организации", "from": "MasterCard 1796816785869527",
         "to": "Visa Classic 7699855375169288"},
        {"id": 360577236, "state": "EXECUTED", "date": "2019-09-07T07:20:13.889610",
         "operationAmount": {"amount": "18536.73", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод с карты на карту", "from": "Maestro 4284341727554246", "to": "МИР 1582474475547301"},
        {"id": 894961746, "state": "EXECUTED", "date": "2019-08-04T20:17:25.443322",
         "operationAmount": {"amount": "2523.44", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод с карты на счет", "from": "Счет 33721541831646393763",
         "to": "Счет 68774571780974952778"},
        {"id": 464419177, "state": "CANCELED", "date": "2018-07-15T18:44:13.346362",
         "operationAmount": {"amount": "71024.64", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод с карты на счет", "from": "Visa Gold 9657499677062945",
         "to": "Счет 19213886662094884261"},
    ]


@pytest.fixture
def executed_list_result():
    return [
        {"id": 894961746, "state": "EXECUTED", "date": "2019-08-04T20:17:25.443322",
         "operationAmount": {"amount": "2523.44", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод с карты на счет", "from": "Счет 33721541831646393763", "to": "Счет 68774571780974952778"},
        {"id": 360577236, "state": "EXECUTED", "date": "2019-09-07T07:20:13.889610",
         "operationAmount": {"amount": "18536.73", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод с карты на карту", "from": "Maestro 4284341727554246", "to": "МИР 1582474475547301"}
    ]

@pytest.fixture
def executed_list_result_0():
    return [
        {"id": 464419177, "state": "CANCELED", "date": "2018-07-15T18:44:13.346362",
         "operationAmount": {"amount": "71024.64", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод с карты на счет", "from": "Visa Gold 9657499677062945",
         "to": "Счет 19213886662094884261"},
        {"id": 894961746, "state": "EXECUTED", "date": "2019-08-04T20:17:25.443322",
         "operationAmount": {"amount": "2523.44", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод с карты на счет", "from": "Счет 33721541831646393763",
         "to": "Счет 68774571780974952778"}
    ]


@pytest.fixture
def canceled_list_result():
    return [
        {"id": 464419177, "state": "CANCELED", "date": "2018-07-15T18:44:13.346362",
         "operationAmount": { "amount": "71024.64", "currency": {"name": "руб.", "code": "RUB"} },
         "description": "Перевод с карты на счет", "from": "Visa Gold 9657499677062945", "to": "Счет 19213886662094884261"},
        {"id": 560813069, "state": "CANCELED", "date": "2019-12-03T04:27:03.427014",
         "operationAmount": { "amount": "17628.50", "currency": {"name": "USD","code": "USD"} },
         "description": "Перевод организации", "from": "MasterCard 1796816785869527", "to": "Visa Classic 7699855375169288"},
    ]


@pytest.fixture
def fixture_filter_by_currency1():
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


@pytest.fixture
def fixture_filter_by_currency2():
    return {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


@pytest.fixture
def fixture_filter_by_currency3():
    return {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {
            "amount": "56883.54",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }

from unittest.mock import patch, Mock
from src.external_api import calculating_transaction_amount


@patch('src.external_api.request_and_conversion')
def test_calculating_rub_transactions(mock_get):
    # Проверка операции в рублях
    operations = [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
              "amount": "100.0",
              "currency": {
                "name": "руб.",
                "code": "RUB"
              }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        }
    ]
    actual_result = calculating_transaction_amount(operations)

    assert actual_result == [100.0]
    assert not mock_get.called, "Не должно быть обращений к API для операций в рублях!"


@patch('src.external_api.request_and_conversion')
def test_calculating_usd_transactions(mock_get):
    # Проверка операции в долларах
    mock_get.return_value = 78.5
    operations = [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "100.0",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    ]
    actual_result = calculating_transaction_amount(operations)

    assert actual_result == [7850.0]
    mock_get.assert_called_once_with("USD")


@patch('src.external_api.request_and_conversion')
def test_missing_operation_data(mock_request_and_conversion):
    # Проверка пропуска некорректных операций
    operations = [
        {},
        {"invalid": True},
        {"operationAmount": {}}
    ]
    actual_result = calculating_transaction_amount(operations)

    assert actual_result == []
    assert not mock_request_and_conversion.called, "Нет обращений к внешнему API."

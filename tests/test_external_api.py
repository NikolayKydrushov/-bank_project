import os

from unittest.mock import patch, Mock
from src.external_api import calculating_transaction_amount
from dotenv import load_dotenv

load_dotenv("../.env")

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
headers = {"apikey": f"{API_KEY}"}


# Тест №1: Операции в рублях (валюта RUB)
@patch('src.external_api.requests.get')
def test_rub_currency_no_api_call(mock_get):
    """
    Тестируем операции в рублях (валюта RUB),
    проверяем, что API не вызывается.
    """
    operations = {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "100.0",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }

    result = calculating_transaction_amount(operations)
    assert result == 100.0
    assert not mock_get.called, "API не должен вызываться для операций в рублях"


# Тест №2: Операции в иностранной валюте (USD)
@patch('src.external_api.requests.get')
def test_foreign_currency_calls_api(mock_get):
    """
    Тестируем операции в иностранной валюте (USD),
    проверяем, что API вызывается и корректно конвертируется сумма.
    """
    # Создаем простой объект типа Mock для ответа от API
    mock_response = Mock()
    mock_response.json.return_value = {"conversion_rates": {"RUB": 78.5}}
    mock_get.return_value = mock_response

    operations = {
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

    result = calculating_transaction_amount(operations)
    assert result == 7850.0
    mock_get.assert_called_once_with(f'{BASE_URL}{API_KEY}/latest/USD', headers=headers)

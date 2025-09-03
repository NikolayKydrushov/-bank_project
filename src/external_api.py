import os

import requests
from dotenv import load_dotenv

from src.utils import open_file

load_dotenv("../.env")

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
# API_KEY=4f4ab138d65eac52a10e8133
# BASE_URL = https://v6.exchangerate-api.com/v6/

directory = "data/operations.json"
data_str = open_file(directory)
headers = {"apikey": f"{API_KEY}"}


def calculating_transaction_amount(operation: dict) -> float:
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.

    Args:
        operation: Словарь транзакции их содержимого в json файле operations

    Returns:
        Возвращает конвертируемую валюту в рублях типа float
    """

    currency_code = operation["operationAmount"]["currency"]["code"]
    url = f"{BASE_URL}{API_KEY}/latest/{currency_code}"
    amount = float(operation["operationAmount"]["amount"])

    if currency_code == "RUB":
        rounded_amount = round(amount, 2)
        return rounded_amount

    else:
        response = requests.get(url, headers=headers)
        response_json = response.json()
        exchange_rate_relative_rub = response_json["conversion_rates"]["RUB"]
        rate = round(float(exchange_rate_relative_rub), 2)

        rounded_amount = round(amount * rate, 2)

    return rounded_amount


# Пример работы функции для конвертации всех операций из operations
# for i in range(len(data_str)):
#     print(calculating_transaction_amount(data_str[i]))

# Пример вызова функции конвертации в рубли
# print(calculating_transaction_amount(data_str[0]))

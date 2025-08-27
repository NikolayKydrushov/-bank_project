import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.utils import directory, open_file

load_dotenv("../.env")

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


data_str = open_file(directory)
headers = {"apikey": f"{API_KEY}"}


def calculating_transaction_amount(operations: Any) -> list[float]:
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.

    Args:
        operations: Список содержимого в json файле operations

    Returns:
        Возвращает список result
    """

    result = []

    for operation in operations:

        if (
            "operationAmount" not in operation
            or "currency" not in operation["operationAmount"]
            or "code" not in operation["operationAmount"]["currency"]
        ):
            continue
        currency_code = operation["operationAmount"]["currency"]["code"]
        amount = float(operation["operationAmount"]["amount"])

        if currency_code == "RUB":
            rounded_amount = round(amount, 2)
            result.append(rounded_amount)

        else:
            rate = round(float(request_and_conversion(currency_code)), 2)
            rounded_amount = round(amount * rate, 2)
            result.append(rounded_amount)

    return result


def request_and_conversion(currency):
    url = f"{BASE_URL}{API_KEY}/latest/{currency}"
    response = requests.get(url, headers=headers)

    response_json = response.json()
    return response_json["conversion_rates"]["RUB"]


try:
    data = json.loads(data_str)
except json.JSONDecodeError as e:
    print(f"Ошибка разбора JSON файла операций: {e}")
else:
    amounts = calculating_transaction_amount(data)
    print(amounts)

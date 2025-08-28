import os

import requests
from dotenv import load_dotenv

from src.utils import directory, open_file

load_dotenv("../.env")

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
# API_KEY=4f4ab138d65eac52a10e8133
# BASE_URL = https://v6.exchangerate-api.com/v6/

data_str = open_file(directory)
headers = {"apikey": f"{API_KEY}"}


def calculating_transaction_amount(operations: list[dict]) -> list[dict]:
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли.

    Args:
        operations: Список содержимого в json файле operations

    Returns:
        Возвращает список result
    """

  # if (
  #       "operationAmount" not in operation
  #       or "currency" not in operation["operationAmount"]
  #       or "code" not in operation["operationAmount"]["currency"]
  #   ):
    result = operations
    for operation in result:
        currency_code = operation["operationAmount"]["currency"]["code"]
        url = f"{BASE_URL}{API_KEY}/latest/{currency_code}"
        amount = float(operation["operationAmount"]["amount"])


        if currency_code == "RUB":
            # rounded_amount = round(amount, 2)
            return result

        else:
            response = requests.get(url, headers=headers)
            response_json = response.json()
            exchange_rate_relative_rub = response_json["conversion_rates"]["RUB"]
            rate = round(float(exchange_rate_relative_rub), 2)

            rounded_amount = round(amount * rate, 2)

            operation["operationAmount"]["currency"]["name"] = "руб."
            operation["operationAmount"]["currency"]["code"] = "RUB"
            operation["operationAmount"]["amount"] = f"{rounded_amount}"

    return result



# try:
#     data = json.loads(data_str)
# except json.JSONDecodeError as e:
#     print(f"Ошибка разбора JSON файла операций: {e}")
# else:
# amounts = calculating_transaction_amount(data_str)
# print(amounts)

# for i in range(len(data_str)):
#     print(calculating_transaction_amount(data_str[i]))
print(calculating_transaction_amount(data_str))

import json
import os
import requests
from src.utils import open_file, directory
from dotenv import load_dotenv

load_dotenv('../.env')

API_KEY = os.getenv('API_KEY')
data_str = open_file(directory)

BASE_URL = os.getenv('BASE_URL')
# external_api
headers = {"apikey": f"{API_KEY}"}


def calculating_transaction_amount(operations):

    result = []

    for operation in operations:

        if ("operationAmount" not in operation or
                "currency" not in operation["operationAmount"] or
                "code" not in operation["operationAmount"]["currency"]):
            continue
        currency_code = operation["operationAmount"]["currency"]["code"]

        if currency_code == "RUB":
            rounded_amount = round(float(operation["operationAmount"]["amount"]), 2)
            result.append(rounded_amount)

        else:
            rate = round(float(request_and_conversion(currency_code)), 2)
            rounded_amount = round(float(operation["operationAmount"]["amount"]) * rate, 2)
            result.append(rounded_amount)

    return result


def request_and_conversion(currency):
    url = f"{BASE_URL}{API_KEY}/latest/{currency}"
    response = requests.get(url, headers=headers)

    response_json = response.json()
    # response_data = json.loads(response_json)
    return response_json["conversion_rates"]["RUB"]



try:
    data = json.loads(data_str)
except json.JSONDecodeError as e:
    print(f'Ошибка разбора JSON файла операций: {e}')
else:
    amounts = calculating_transaction_amount(data)
    print(amounts)
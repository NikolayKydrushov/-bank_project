from typing import Generator, Any

transactions = [
    {
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
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "1234.56",
            "currency": {"name": "EUR", "code": "EUR"},
        },
        "description": "Покупка товаров",
        "from": "Счет 12345678901234567890",
        "to": "Поставщик X",
    },
    {
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
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {
            "amount": "500.00",
            "currency": {"name": "RUB", "code": "RUB"},
        },
        "description": "Комиссия за обслуживание",
        "from": "Счет 99999999999999999999",
        "to": "Банк",
    },
]


def filter_by_currency(transactions: list[dict],
                       currency: str) -> Generator[dict, Any, None]:

    if len(transactions) > 0 and not currency == None:
        for transaction in transactions:
            if (
                "operationAmount" in transaction
                and "currency" in transaction["operationAmount"]
                and "code" in transaction["operationAmount"]["currency"]
            ):
                if transaction["operationAmount"]["currency"]["code"] == currency:
                    yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[dict, Any, None]:
    if len(transactions) > 0:
        for transaction in transactions:
            yield transaction["description"]


def card_number_generator(initial_values: Any,
                          final_values: Any) -> Generator[str, Any, None]:

    if not initial_values == None and not final_values == None:
        for i in range(initial_values, final_values + 1):
            card_number = str(i)
            number_zeros = 16 - len(card_number)
            string_with_zeros = "0" * number_zeros
            str_card = string_with_zeros + card_number
            yield f"{str_card[:4]} {str_card[4:8]} {str_card[8:12]} {str_card[12:16]}"

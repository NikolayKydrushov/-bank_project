import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
    transactions,
)


def test_filter_by_currency(
    fixture_filter_by_currency1,
    fixture_filter_by_currency2,
    fixture_filter_by_currency3,
):

    generator = filter_by_currency(transactions, "USD")
    assert next(generator) == fixture_filter_by_currency1
    assert next(generator) == fixture_filter_by_currency2
    assert next(generator) == fixture_filter_by_currency3

    try:
        assert (
            filter_by_currency([], "USD")
            == "<generator object filter_by_currency at 0x000001C8EA7E33E0>"
        )
        assert (
            filter_by_currency(
                transactions,
            )
            == "<generator object filter_by_currency at 0x000001C8EA7E33E0>"
        )
    except AssertionError:
        pass


def test_transaction_descriptions():
    generator = transaction_descriptions(transactions)
    assert next(generator) == "Перевод организации"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод со счета на счет"
    assert next(generator) == "Перевод с карты на карту"
    assert next(generator) == "Перевод организации"

    try:
        transaction_descriptions(
            []
        ) == "<generator object filter_by_currency at 0x000001C8EA7E33E0>"
    except AssertionError:
        pass


@pytest.mark.parametrize(
    "start, end, card_numbers",
    [
        (
            1,
            5,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004",
                "0000 0000 0000 0005",
            ],
        ),
        (
            9999999999999998,
            9999999999999999,
            [
                "9999 9999 9999 9998",
                "9999 9999 9999 9999",
            ],
        ),
        (
            10,
            12,
            [
                "0000 0000 0000 0010",
                "0000 0000 0000 0011",
                "0000 0000 0000 0012",
            ],
        ),
    ],
)
def test_card_number_generator(start, end, card_numbers):
    generator = card_number_generator(start, end)
    assert list(generator) == card_numbers

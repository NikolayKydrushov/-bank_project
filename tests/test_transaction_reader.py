import os
from unittest.mock import patch

import pandas as pd
import pytest

from dotenv import load_dotenv

# load_dotenv("../.env")
#
# PATH_CSV_FILE = os.getenv("PATH_CSV_FILE")
# PATH_XLSX_FILE = os.getenv("PATH_XLSX_FILE")

from src.transaction_reader import csv_reader, xlsx_reader


@pytest.fixture
def transactions():
    return [
            {
                'id': 650703.0,
                'state': 'EXECUTED',
                'date': '2023-09-05T11:30:32Z',
                'amount': 16210.0,
                'currency_name': 'Sol',
                'currency_code': 'PEN',
                'from': 'Счет 58803664561298323391',
                'to': 'Счет 39745660563456619397',
                'description': 'Перевод организации'
            },

            {
                'id': 3598919.0,
                'state': 'EXECUTED',
                'date': '2020-12-06T23:00:58Z',
                'amount': 29740.0,
                'currency_name': 'Peso',
                'currency_code': 'COP',
                'from': 'Discover 3172601889670065',
                'to': 'Discover 0720428384694643',
                'description': 'Перевод с карты на карту'
            }
        ]

# Тест №1: Проверка открытия csv файла
@patch("pandas.read_csv")
def test_read_csv(mock_read_csv, transactions):

    mock_read_csv.return_value = pd.DataFrame(transactions)

    # Запуск функции с любым именем файла
    result = csv_reader('date/fake/file.csv')

    # Проверка правильности возвращаемого результата
    assert isinstance(result, list)
    assert result == transactions


# Тест №2: Проверка открытия пустого csv файла
@patch("pandas.read_csv")
def test_read_empty_csv(mock_read_csv):

    empty_df  = pd.DataFrame(columns = [])
    mock_read_csv.return_value = empty_df

    fake_file_path = "empty_file.csv"

    # Получаем результат вызова функции
    result = csv_reader(fake_file_path)

    # Проверяем, что функция вернула пустой список
    assert isinstance(result, list)
    assert result == []


# Тест №3: Проверка открытия excel файла
@patch('pandas.read_excel')
def test_xlsx_reader(mock_read_csv, transactions):

    mock_read_csv.return_value = pd.DataFrame(transactions)

    # Запуск функции с любым именем файла
    result = xlsx_reader('date/fake/file.xlsx')

    # Проверка правильности возвращаемого результата
    assert isinstance(result, list)
    assert result == transactions


# Тест №4: Проверка открытия пустого excel файла
@patch("pandas.read_excel")
def test_xlsx_empty_reader(mock_read_xlsx):

    empty_df  = pd.DataFrame(columns = [])
    mock_read_xlsx.return_value = empty_df

    fake_file_path = "empty_file.xlsx"

    # Получаем результат вызова функции
    result = xlsx_reader(fake_file_path)

    # Проверяем, что функция вернула пустой список
    assert isinstance(result, list)
    assert result == []


# Тест №5: Проверка исключения для несуществующего файла
def test_nonexistent_file():
    nonexistent_file_path = "file/doesnot/exist.csv"

    try:
        csv_reader(nonexistent_file_path)
    except Exception as e:
        assert isinstance(e, FileNotFoundError), "Ожидалось исключение FileNotFoundError"
    else:
        AssertionError("Нет ошибки при открытии несуществующего файла!")


# Тест №6: Проверка неправильного формата файла
def test_invalid_format():
    invalid_file_path = "invalid_format.xls"

    try:
        xlsx_reader(invalid_file_path)
    except IOError as e:
        # Предположим, что тут ошибка ввода-вывода произошла
        assert True, "Исключение IOError было вызвано"
    except Exception as other_e:
        # Любое другое исключение недопустимо
        assert False, f"Получено неожиданное исключение: {other_e}"
    else:
        raise AssertionError("Нет ошибки при попытке открыть неподдерживаемый формат файла!")
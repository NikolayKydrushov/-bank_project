import time

import os
import pandas as pd
# from dotenv import load_dotenv
#
# load_dotenv("../.env")
#
# PATH_CSV_FILE = os.getenv("PATH_CSV_FILE")
# PATH_XLSX_FILE = os.getenv("PATH_XLSX_FILE")

PATH_CSV_FILE = "data/transactions.csv"
PATH_XLSX_FILE = 'data/transactions_excel.xlsx'


def csv_reader(file_path: str) -> list[dict]:
    """
    Функция открытия и чтения файла transactions.csv

    Args:
        file_path: Путь до файла transactions.csv

    Returns:
        Возвращает список словарей с данными из указанного файла
    """
    try:
        reader_csv = pd.read_csv(file_path)
        # print(reader_csv.head())
        return reader_csv.to_dict("records")
    except FileNotFoundError:
        return []
    except TypeError:
        return []
    except ValueError:
        return []


def xlsx_reader(file_path: str) -> list[dict]:
    """
    Функция открытия и чтения файла transactions_excel.xlsx

    Args:
        file_path: Путь до файла transactions_excel.xlsx

    Returns:
        Возвращает список словарей с данными из указанного файла
    """
    reader_xlsx = pd.read_excel(file_path)
    # print(reader_xlsx.head())
    return reader_xlsx.to_dict("records")


# print(csv_reader(str(PATH_CSV_FILE)))
# time.sleep(3)
# print(xlsx_reader(str(PATH_XLSX_FILE)))

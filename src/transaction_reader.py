from dotenv import load_dotenv

import os
import time
import pandas as pd

load_dotenv("../.env")

PATH_CSV_FILE = os.getenv("PATH_CSV_FILE")
PATH_XLSX_FILE = os.getenv("PATH_XLSX_FILE")

"""
Нужно написать функции, которые будут считывать данные из CSV- и XLSX-файлов.
Эти функции должны возвращать список словарей,
где каждый словарь представляет собой одну транзакцию с соответствующими полями из файла.
Обрати внимание на структуру данных и какие поля должны быть включены в словарь.
"""

def csv_reader(file_path: str) -> list[dict]:
    """
    Функция открытия и чтения файла transactions.csv

    Args:
        file_path: Путь до файла transactions.csv

    Returns:
        Возвращает список словарей с данными из указанного файла
    """
    reader_csv = pd.read_csv(file_path)
    # print(reader_csv.head())
    return reader_csv.to_dict('records')



def xlsx_reader(file_path: str) -> list[dict]:
    """
    Функция открытия и чтения файла transactions.csv

    Args:
        file_path: Путь до файла transactions_excel.xlsx

    Returns:
        Возвращает список словарей с данными из указанного файла
    """
    reader_xlsx = pd.read_excel(file_path)
    # print(reader_xlsx.head())
    return reader_xlsx.to_dict('records')


print(csv_reader(PATH_CSV_FILE), end='\n\n\n')
time.sleep(3)
print(xlsx_reader(PATH_XLSX_FILE))


"""
    [
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
"""
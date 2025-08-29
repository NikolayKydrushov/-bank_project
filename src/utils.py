import json
import logging

logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/utils.log', mode='w', encoding ="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def open_file(file_: str) -> list[dict]:
    """
    Функция чтения json файла operations и преобразования его в словарь.

    Args:
        file_: Путь к файлу

    Returns:
        Возвращает список словарей data из json файла operations.
    """
    try:
        logger.info('Открытие json файла operations')
        with open(file_, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info('Успешное преобразование данных')
            return data

    except json.JSONDecodeError as js_:
        logger.info(f'Ошибка {js_}')
        return []
    except FileNotFoundError as fnf:
        logger.error(f'Ошибка {fnf}')
        return []
    except TypeError as te:
        logger.error(f'Ошибка {te}')
        return []
    except ValueError as ve:
        logger.error(f'Ошибка {ve}')
        return []


directory = "data/operations.json"
result = open_file(directory)
print(result)

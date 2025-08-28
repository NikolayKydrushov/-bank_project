import json


def open_file(file: str) -> list:
    """
    Функция чтения json файла operations и преобразования его в словарь

    Args:
        file: Путь к файлу

    Returns:
        Возвращает список date
    """
    try:
        with open(file, "r", encoding="utf-8") as f:
            date = json.load(f)
            return date
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    except TypeError:
        return []
    except ValueError:
        return []


directory = "C:/Skypro/showing_recent_successful_operations/data/operations.json"

import json


def open_file(file_: str) -> list[dict]:
    """
    Функция чтения json файла operations и преобразования его в словарь.

    Args:
        file_: Путь к файлу

    Returns:
        Возвращает список словарей data из json файла operations.
    """
    try:
        with open(file_, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data

    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []
    except TypeError:
        return []
    except ValueError:
        return []


directory = "data/operations.json"
result = open_file(directory)
print(result)

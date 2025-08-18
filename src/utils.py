import json
import os




def open_file(file):

    try:
        with open(file, "r", encoding='utf-8') as f:
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

directory = 'C:/Skypro/showing_recent_successful_operations/data'

file_path = os.path.join(directory, 'operations.json')

print(f'Полный путь к файлу: {file_path}')

print(open_file(file_path))
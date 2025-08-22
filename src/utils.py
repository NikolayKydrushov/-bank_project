import json
import os
from dotenv import load_dotenv



def open_file(file: str) -> list:

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
#
# file_path = os.path.join(directory, "operations.json")

print(open_file(directory))

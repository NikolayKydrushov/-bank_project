import re
from collections import Counter


def filter_by_state(list_: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и опционально значение для ключа

    Args:
        list_: Список словарей
        state: Ключ, по умолчанию 'EXECUTED'

    Returns:
        Функция возвращает новый список словарей, содержащий только те словари,
        у которых ключ state соответствует указанному значению.
    """

    if (len(list_) > 0 and (state == "EXECUTED" or state == "CANCELED" or state == "PENDING")):
        identical_keys = []
        for i in list_:
            if i.get("state") == state:
                identical_keys.append(i)

        return identical_keys
    return []


def sort_by_date(date: list[dict], order: bool = True) -> list[dict]:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки

    Args:
        date: Список словарей
        order: Значение сортировки

    Returns:
        Функция возвращает новый список, отсортированный по дате.
    """
    if len(date) > 0 or order is not None:
        sorted_date = date[:]

        sorted_date.sort(key=lambda x: x["date"], reverse=order)

        return sorted_date
    return []


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция, которая принимает список словарей с данными о банковских операциях и строку поиска.
    А возвращает список словарей, в описании которых есть данная строка.

    Args:
        data: Список словарей с данными о банковских операциях
        search: Строка поиска
    Returns:
        Возвращает список словарей, в описании которых есть искомая строка.
    """
    if not data:
        return []
    else:
        new_data_list = []

        pattern = re.compile(search, flags=re.IGNORECASE)

        for operation in data:

            description = operation.get("description", "")

            if pattern.search(description):
                new_data_list.append(operation)

        print(len(new_data_list))
        return new_data_list


# print(process_bank_search(transactions, "Перевод с карты на карту"))


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция, которая будет принимать список словарей с данными о банковских операциях
    и список категорий операций. Возвращать словарь, в котором ключи — это названия категорий.

    Args:
        data: Список словарей с данными о банковских операциях
        categories: Список категорий операций
    Returns:
        Возвращает словарь, в котором {key : value} это
        {название категорий: кол-во операций в каждой категории}
    """
    if not data:
        return {}
    else:
        new_data_dict = []

        for operation in data:

            description = operation.get("description", "").lower()

            for category in categories:

                if re.search(category.lower(), description):
                    new_data_dict.append(category)

        result = Counter(new_data_dict)

        return result


# list_r = ["Перевод с карты на карту", "Перевод организации", "Перевод со счета на счет"]
# print(process_bank_operations(transactions, list_r))

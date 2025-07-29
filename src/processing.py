def filter_by_state(list_, state="EXECUTED"):
    """
    Функция принимает список словарей и опционально значение для ключа

    Args:
        list_: Список словарей
        state: Ключ, по умолчанию 'EXECUTED'

    Returns:
        Функция возвращает новый список словарей, содержащий только те словари,
        у которых ключ state соответствует указанному значению.
    """

    identical_keys = []
    for i in range(len(list_)):
        if list_[i]["state"] == state:
            identical_keys.append(list_[i])

    return identical_keys


def sort_by_date(date: list[dict], order: bool = True) -> list[dict]:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки

    Args:
        date: Список словарей
        order: Значение сортировки

    Returns:
        Функция возвращает новый список, отсортированный по дате.
    """
    sorted_date = date[:]

    sorted_date.sort(key=lambda x: x["date"], reverse=order)

    return sorted_date

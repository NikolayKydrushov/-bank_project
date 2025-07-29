def filter_by_state(list_, state = 'EXECUTED'):
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
        if list_[i]['state'] == state:
            identical_keys.append(list_[i])

    return identical_keys


def sort_by_date(list_, date):
    pass
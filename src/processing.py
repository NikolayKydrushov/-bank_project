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

filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}])

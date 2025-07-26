from typing import Union

from src import masks as f


def mask_account_card(card_or_account_number: Union[str]) -> str:
    """
    Функция маскировки номера банковской карты или счета

    Args:
        card_or_account_number: Номер карты или счета

    Returns:
        Маску номера карты, где видны первые 6 цифр и последние 4 цифры остальные символы отображаются *.
        Номер разбит по блокам по 4 цифры, разделенным пробелами.
        Маску номера счета, где видны только последние 4 цифры номера, а перед ними — две *.
    """

    separation = card_or_account_number.split(", ")

    if separation[0] == "Счет":
        separation[-1] = f.get_mask_account(separation[-1])
    else:
        separation[-1] = f.get_mask_card_number(separation[-1])

    res = " ".join(separation)
    return res


def get_date(date: Union[str]) -> str:
    """
    Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ".

    Args:
        date: Строка в формате: "Год, месяц, число, время".

    Returns:
        Строку в формате "ДД.ММ.ГГГГ".
    """
    final_line = date[8:10] + date[5:7] + date[:5]

    return final_line

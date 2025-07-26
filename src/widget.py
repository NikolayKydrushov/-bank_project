from src import masks as f


def mask_account_card(card_or_account_number):
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

    res = ' '.join(separation)
    return res
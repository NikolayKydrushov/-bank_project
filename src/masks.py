from typing import Union


def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Функция маскировки номера банковской карты

    Args:
        card_number: Номер карты

    Returns:
        Маску номера карты, где видны первые 6 цифр и последние 4 цифры остальные символы отображаются *.
        Номер разбит по блокам по 4 цифры, разделенным пробелами.
    """
    card_number = str(card_number)

    first_index = 0
    last_index = 4
    number_with_spaces = ""

    if card_number.isdigit():
        if len(card_number) == 16:

            for i in range(4):
                number_with_spaces += card_number[first_index:last_index] + " "
                first_index += 4
                last_index += 4

            number_with_spaces_and_asterisks = (
                number_with_spaces[:7] + "** ****" + number_with_spaces[14:-1]
            )

            return number_with_spaces_and_asterisks

    return "Длина номера карты неправильна"


def get_mask_account(account_number: Union[str, int]) -> str:
    """
    Функция маскировки номера банковского счета

    Args:
        account_number: Номер счета

    Returns:
        Маску номера счета, где видны только последние 4 цифры номера, а перед ними — две *.
    """
    account_number = str(account_number)

    if account_number.isdigit():
        if len(account_number) == 20:

            last_four_characters = account_number[-4:]
            last_four_characters_with_asterisks = "**" + last_four_characters

            return last_four_characters_with_asterisks

    return "Длина номера карты неправильна"

from typing import Union
import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/masks.log', mode='w', encoding ="utf-8")
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


# Реализуйте запись логов в файл. Логи должны записываться в папку
# logs в корне проекта. Файлы логов должны иметь расширение .log.

# Формат записи лога в файл должен включать
    # метку времени,
    # название модуля,
    # уровень серьезности и
    # сообщение, описывающее событие или ошибку, которые произошли.

# Лог должен перезаписываться при каждом запуске приложения.

def get_mask_card_number(card_number: Union[str, int]) -> str:
    """
    Функция маскировки номера банковской карты

    Args:
        card_number: Номер карты

    Returns:
        Маску номера карты, где видны первые 6 цифр и последние 4 цифры остальные символы отображаются *.
        Номер разбит по блокам по 4 цифры, разделенным пробелами.
    """
    logger.info('Перевод номера карты в строку')
    card_number = str(card_number)

    first_index = 0
    last_index = 4
    number_with_spaces = ""

    if card_number.isdigit():
        logger.info('Проверка корректной длины номера карты')
        if len(card_number) == 16:

            for i in range(4):
                number_with_spaces += card_number[first_index:last_index] + " "
                first_index += 4
                last_index += 4

            logger.info('Маскировка номера карты')
            number_with_spaces_and_asterisks = (
                number_with_spaces[:7] + "** ****" + number_with_spaces[14:-1]
            )

            return number_with_spaces_and_asterisks

    logger.warning('Длина номера карты неправильна')
    return "Длина номера карты неправильна"


def get_mask_account(account_number: Union[str, int]) -> str:
    """
    Функция маскировки номера банковского счета

    Args:
        account_number: Номер счета

    Returns:
        Маску номера счета, где видны только последние 4 цифры номера, а перед ними — две *.
    """
    logger.info('Перевод номера счета в строку')
    account_number = str(account_number)

    if account_number.isdigit():
        logger.info('Проверка корректной длины номера счета')
        if len(account_number) == 20:

            logger.info('Маскировка номера карты')
            last_four_characters = account_number[-4:]
            last_four_characters_with_asterisks = "**" + last_four_characters

            return last_four_characters_with_asterisks

    logger.warning('Длина номера счета неправильна')
    return "Длина номера счета неправильна"


get_mask_card_number("7158300734726758")
get_mask_account("64686473678894779589")
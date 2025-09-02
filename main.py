# from src import masks as f
#
# if __name__ == '__main__':
#     print(f.get_mask_card_number(7000792289606361))
#     print(f.get_mask_account(73654108430135874305))

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date, process_bank_search
from src.transaction_reader import csv_reader, xlsx_reader
from src.utils import open_file
from src.widget import get_date, mask_account_card

opening_file = None
filter_data = None
sort_date = None


def main() -> None:
    global opening_file, filter_data, sort_date
    hello_text = (
        "Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями. \n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )
    # Открытие файла того формата, который задаст пользователь
    files_and_paths = {
        1: {
            "message": "Для обработки выбран JSON-файл.",
            "path": "src/data/operations.json",
        },
        2: {
            "message": "Для обработки выбран CSV-файл",
            "path": "src/data/transactions.csv",
        },
        3: {
            "message": "Для обработки выбран XLSX-файла.",
            "path": "src/data/transactions_excel.xlsx",
        },
    }

    while True:
        print(hello_text)

        try:

            result = int(input("Пользователь: "))
            file_data = files_and_paths[result]
            print(f"Программа: {file_data['message']}")
            if files_and_paths[result] == 1:
                opening_file = open_file(file_data["path"])

            elif files_and_paths[result] == 2:
                opening_file = csv_reader(file_data["path"])

            elif files_and_paths[result] == 3:
                opening_file = xlsx_reader(file_data["path"])

            break

        except KeyError:
            print("Неверный номер, повторите еще раз")

    # Фильтрация по выбранному статусу
    filtering_list = ["EXECUTED", "CANCELED", "PENDIN"]

    while True:
        print(
            "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )

        filtering_status = str(input("Пользователь: "))

        if filtering_status.upper() in filtering_list:
            print(
                f"Программа: Операции отфильтрованы по статусу {filtering_status.upper()}"
            )
            filter_data = filter_by_state(opening_file, filtering_status.upper())
            break
        else:
            print(f'Статус операции "{filtering_status}" недоступен.')

    # Уточняющие вопросу пользователю
    program_questions = [
        ("Отсортировать операции по дате? (Да/Нет)", ["да", "нет"]),
        (
            "Отсортировать по возрастанию или по убыванию?",
            [
                "возрастание",
                "убывание",
                "возрастанию",
                "убыванию",
                "повозрастанию",
                "поубыванию",
            ],
        ),
        ("Выводить только рублевые транзакции? (Да/Нет)", ["да", "нет"]),
        (
            "Отфильтровать список транзакций по определенному слову в описании? (Да/Нет)",
            ["да", "нет"],
        ),
    ]

    user_responses = []
    for question, possible_answers in program_questions:
        while True:
            print(f"Программа: {question}")
            answer = input("Пользователь: ").strip().lower()
            if answer in possible_answers:
                user_responses.append(answer)
                break
            else:
                print("Ошибка: неверный ответ. Попробуйте снова.")

    print("Программа: Распечатываю итоговый список транзакций...")

    # Сортировке по дате по убыванию или по возрастанию

    backup_data_filter = filter_data[:]
    flag = user_responses[1] == "возрастание" or user_responses[1] == "возрастанию"

    if user_responses[0] == "да":
        if user_responses[1] == "да":
            backup_data_filter = sort_by_date(backup_data_filter, flag)

    # Сортировка только рублевых транзакций
    if user_responses[2] == "да" and user_responses[0] == "да":
        backup_data_filter = list(filter_by_currency(backup_data_filter, "RUB"))

    # Сортировка по определенному слову в описании
    if user_responses[3] == "да":
        search_word = str(
            input("Программа: Введите слово для поиска в описаниях транзакций: ")
        )
        backup_data_filter = process_bank_search(backup_data_filter, search_word)

    filter_data = backup_data_filter

    # Вывод кол-ва найденных транзакций или сообщение об отсутствии транзакций по заданным параметрам
    message = f"Программа:\nВсего банковских операций в выборке: {len(filter_data)}"
    if not filter_data:
        message = "Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации"
    print(message)

    # Вывод транзакций в формате:
    # Дата в формате "ДД.ММ.ГГГГ" Описание транзакции
    # Откуда -> Куда
    # Сумма: число валюта

    for item in filter_data:
        date_open = get_date(item["date"])
        date_and_desc = f"\n{date_open} {item["description"]}"

        if item["description"] == "Открытие вклада":
            translation = f"{mask_account_card(item["to"])}"
        else:
            translation = (
                f"{mask_account_card(item["from"])} -> {mask_account_card(item["to"])}"
            )
        sum_currency = (f"{item["operationAmount"]["amount"]} "
                        f"{item["operationAmount"]["currency"]["code"]} "
                        f"{item["operationAmount"]["currency"]["name"]}")

        print(f"{date_and_desc}\n {translation} \nСумма: {sum_currency}")

    return None


if __name__ == "__main__":
    main()

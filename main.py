import os

from src.file_readers import read_csv_file, read_xlsx_file
from src.processing import filter_by_state, sort_by_date
from src.utils import process_bank_search, read_file_json
from src.widget import get_date, mask_account_card


def main():

    print(
        """\
Привет! Добро пожаловать в программу работы
с банковскими транзакциями.\n\
"""
    )

    while True:

        selected_option_opening_file = input(
            """\
Выберите необходимый пункт меню:

1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла

Ввод: \
"""
        )
        # Блок выбора типа файла с которым планируется работа
        if selected_option_opening_file == "1":
            print("\nДля обработки выбран JSON-файл")
            file_info = read_file_json(os.path.join(os.path.dirname(__file__), "data", "operations.json"))
            break
        elif selected_option_opening_file == "2":
            print("\nДля обработки выбран CSV-файл")
            file_info = read_csv_file(os.path.join(os.path.dirname(__file__), "data", "transactions.csv"))
            break
        elif selected_option_opening_file == "3":
            print("\nДля обработки выбран XLSX-файл")
            file_info = read_xlsx_file(os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx"))
            break
        else:
            print(f"\nПункта {selected_option_opening_file} не существует\n")
    # Блок выбора статуса транзакций, для фильтрации списка всех транзакций
    while True:
        selected_option_status = input(
            "\nВведите статус, по которому необходимо выполнить фильтрацию.\n\
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nВвод: "
        ).upper()

        if selected_option_status not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"\nСтатус операции {selected_option_status} недоступен.")
        else:
            print(f"\nОперации отфильтрованы по статусу {selected_option_status}")
            result_filter = filter_by_state(file_info, selected_option_status)
            break
    # Блок выбора нужно ли сортировать полученный список по дате, если нужно то в каком направлении
    while True:
        choice_sort_by_date = input("\nОтсортировать операции по дате? Да/Нет\nВвод: ")
        if choice_sort_by_date.lower() == "да":
            sorting_direction = input("\nОтсортировать по возрастанию или по убыванию?\nВвод: ").lower()

            while True:
                if sorting_direction == "по возрастанию":
                    result_filter = sort_by_date(result_filter, reverse_state=False)
                    break
                elif sorting_direction == "по убыванию":
                    result_filter = sort_by_date(result_filter)
                    break
                else:
                    print("Неправильно указано направление сортировки")
            break
        elif choice_sort_by_date.lower() == "нет":
            break
        else:
            print(f"Нет варианта {choice_sort_by_date}")
    # Блок выбора необходимости вывести только рублевые операции
    while True:
        choice_sort_by_currency_rub = input("\nВыводить только рублевые транзакции? Да/Нет\nВвод: ")
        if choice_sort_by_currency_rub.lower() == "да":
            if selected_option_opening_file == "1":
                result_filter = [
                    currency for currency in result_filter if currency["operationAmount"]["currency"]["code"] == "RUB"
                ]
            elif selected_option_opening_file == "2" or selected_option_opening_file == "3":
                result_filter = [currency for currency in result_filter if currency.get("currency_code") == "RUB"]
            break
        elif choice_sort_by_currency_rub.lower() == "нет":
            break
        else:
            print(f"Нет варианта {choice_sort_by_currency_rub}")
    # Блок выбора нужно ли сортировать полученный список по определенному слову в описании, если то по какому
    while True:
        sort_by_key_word = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\nВвод: ")
        if sort_by_key_word.lower() == "да":
            key_word = input("\nВведите слово для фильтрации.\nВвод: ")
            result_filter = process_bank_search(result_filter, key_word)
            break
        elif sort_by_key_word.lower() == "нет":
            break
        else:
            print(f"Нет варианта {sort_by_key_word}")

    result_list_transactions = []
    # Блок получения данных, необходимых для формирования выходных данных, из списка отфильтрованных транзакций
    for elem in result_filter:
        if selected_option_opening_file == "1":
            date_transactions = get_date(elem.get("date"))
            amount_transaction = elem.get("operationAmount").get("amount")
            state_transaction = elem.get("description")
            from_transaction = mask_account_card(elem.get("from"))
            to_transaction = mask_account_card(elem.get("to"))
            currency_transaction = elem["operationAmount"]["currency"]["name"]
        else:
            date_transactions = get_date(elem.get("date"))
            amount_transaction = elem.get("amount")
            state_transaction = elem.get("description")
            from_transaction = mask_account_card(elem.get("from"))
            to_transaction = mask_account_card(elem.get("to"))
            currency_transaction = elem["currency_code"]

        if state_transaction == "Открытие вклада":
            result_list_transactions.append(
                f"{date_transactions} {state_transaction}\n"
                f"{to_transaction}\n"
                f"Сумма: {amount_transaction} {currency_transaction}\n"
            )
        else:
            result_list_transactions.append(
                f"{date_transactions} {state_transaction}\n"
                f"{from_transaction} -> {to_transaction}\n"
                f"Сумма: {amount_transaction} {currency_transaction}\n"
            )
    # Вывод результата
    if result_filter:
        print("Распечатываю итоговый список транзакций...\n")
        print(f"Всего банковских операций в выборке: {len(result_filter)}\n")

        for transaction in result_list_transactions:
            print(transaction)

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()

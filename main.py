import os
from pprint import pprint

from src.file_readers import read_xlsx_file, read_csv_file
from src.processing import filter_by_state, sort_by_date
from src.utils import read_file_json


def main():

    print(
'''\
Привет! Добро пожаловать в программу работы 
с банковскими транзакциями.\n\
'''
        )

    while True:

        selected_option_opening_file = input(
'''\
Выберите необходимый пункт меню:

1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
    
Ввод: \
'''
        )

        if selected_option_opening_file == '1':
            print('\nДля обработки выбран JSON-файл')
            file_info = read_file_json(os.path.join(os.path.dirname(__file__), 'data', 'operations.json'))
            break
        elif selected_option_opening_file == '2':
            print('\nДля обработки выбран CSV-файл')
            file_info = read_csv_file(os.path.join(os.path.dirname(__file__), 'data', 'transactions.csv'))
            break
        elif selected_option_opening_file == '3':
            print('\nДля обработки выбран XLSX-файл')
            file_info = read_xlsx_file(os.path.join(os.path.dirname(__file__), 'data', 'transactions_excel.xlsx'))
            break
        else:
            print(f'\nПункта {selected_option_opening_file} не существует\n')

    # pprint(file_info)

    while True:
        selected_option_status = input('\nВведите статус, по которому необходимо выполнить фильтрацию.\n\
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nВвод: ').upper()

        if selected_option_status not in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'\nСтатус операции {selected_option_status} недоступен.')
        else:
            print(f'\nОперации отфильтрованы по статусу {selected_option_status}')
            result_filter = filter_by_state(file_info, selected_option_status)
            break

    choice_sort_by_date = input('\nОтсортировать операции по дате? Да/Нет\nВвод: ')

    if choice_sort_by_date.lower() == 'да':

        while True:
            sorting_direction = input('\nОтсортировать по возрастанию или по убыванию?\nВвод: ').lower()

            if sorting_direction == 'по возрастанию':
                result_filter = sort_by_date(result_filter, reverse_state=False)
                break
            elif sorting_direction == 'по убыванию':
                result_filter = sort_by_date(result_filter)
                break
            else:
                print(f'Неправильно указано направление сортировки')

    choice_sort_by_currency_rub = input('\nВыводить только рублевые транзакции? Да/Нет\nВвод: ')

    if choice_sort_by_currency_rub.lower() == 'да':
        if selected_option_opening_file == '1':
            result_filter = [
                currency
                for currency in result_filter
                if currency['operationAmount']['currency']['code'] == 'RUB'
            ]
        elif selected_option_opening_file == '2' or selected_option_opening_file == '3':
            result_filter = [
                currency
                for currency in result_filter
                if currency.get("currency_code") == 'RUB'
            ]

    return result_filter

if __name__ == "__main__":
    pprint(main())
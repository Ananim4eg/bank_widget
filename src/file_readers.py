import csv

import pandas as pd


def read_csv_file(path_file: str) -> list[dict] | str:
    """Считывает csv файл и возвращает список словарей с транзакциями"""

    try:
        with open(path_file, encoding='utf-8') as csv_file:
            result = csv.DictReader(csv_file, delimiter=';')

            return [row for row in result]

    except FileNotFoundError:
        return 'Файл не найден'


def read_xlsx_file(path_file: str) -> list[dict] | str:
    """Считывает xlsx файл и возвращает список словарей с транзакциями"""

    try:
        excel_data = pd.read_excel(path_file)

        return list(excel_data.to_dict(orient='records'))

    except FileNotFoundError:
        return 'Файл не найден'

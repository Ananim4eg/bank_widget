import csv
import pandas as pd


def read_csv_file(path_file: str) -> list[dict]:
    """Считывает csv файл и возвращает список словарей с транзакциями"""

    with open(path_file, encoding='utf-8') as csv_file:
        result = csv.DictReader(csv_file, delimiter=';')
        next(result)

        return [row for row in result]

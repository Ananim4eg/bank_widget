from json import load, JSONDecodeError


def read_file_json(path_file: str) -> list:
    """
    Принимает путь к json-файлу в качестве аргумента.
    Возвращает список словарей с данными о финансовых транзакциях или, если
    файл пустой, содержит не-список или не найден, возвращается пустой список.
    """

    try:
        with open(path_file, encoding="utf-8") as file_with_operations:

            try:
                list_info_transactions: list = load(file_with_operations)

                if type(list_info_transactions) is not list:
                    return []

                return list_info_transactions

            except JSONDecodeError:
                return []

    except FileNotFoundError:
        return []

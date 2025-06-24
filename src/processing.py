import re
from datetime import datetime
from typing import List, Union


def filter_by_state(my_list: List[dict], filter_parameter: str = "EXECUTED") -> List[dict]:
    """Функция фильтрует список по указанному значению параметра state"""
    new_list = []

    for elem in my_list:
        if elem.get("state") == filter_parameter:
            new_list.append(elem)

    return new_list


def sort_by_date(my_list: List[dict], reverse_state: bool = True) -> Union[List[dict], str]:
    """Функция сортирует список со словарями по ключу data"""
    if not isinstance(reverse_state, bool):
        reverse_state = True

    pattern = r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}"

    try:
        for dict_with_date in my_list:
            if re.fullmatch(pattern, dict_with_date["date"]):
                datetime.strptime(dict_with_date["date"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                datetime.strptime(dict_with_date["date"], "%Y-%m-%dT%H:%M:%SZ")

        new_list = sorted(my_list, key=lambda x: x["date"], reverse=reverse_state)
        return new_list

    except ValueError:

        return "Один или несколько словарей содержат дату в неправильном формате"

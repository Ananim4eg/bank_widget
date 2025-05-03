from typing import List


def filter_by_state(my_list: List[dict], filter_parameter: str = "EXECUTED") -> List[dict]:
    """Функция фильтрует список по указанному значению параметра state"""
    new_list = []

    for elem in my_list:
        if elem["state"] == filter_parameter:
            new_list.append(elem)

    return new_list


def sort_by_date(my_list: List[dict], reverse_state: bool = True) -> List[dict]:
    """Функция сортирует список со словарями по ключу data"""

    new_list = sorted(my_list, key=lambda x: x["date"], reverse=reverse_state)

    return new_list

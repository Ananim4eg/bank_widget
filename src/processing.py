from typing import List


def filter_by_state(my_list: List[dict], filter_parameter: str='EXECUTED') -> List[dict]:
    """Функция фильтрует список по указанному значению параметра state"""
    new_list =[]

    for elem in my_list:
        if elem["state"] == filter_parameter:
            new_list.append(elem)

    return new_list


def sort_by_date(my_list: List[dict], reverse=False) -> List[dict]:
    new_list = []

    return new_list

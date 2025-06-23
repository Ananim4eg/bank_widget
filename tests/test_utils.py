from json import loads
from unittest.mock import patch, mock_open

from src.utils import read_file_json, process_bank_search, process_bank_operations

test_data = """[{
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }]"""

test_list = [{
    "id": 716496732,
    "state": "EXECUTED",
    "date": "2018-04-04T17:33:34.701093",
    "operationAmount": {
      "amount": "40701.91",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Gold 5999414228426353",
    "to": "Счет 72731966109147704472"
  },
  {
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  },
  {
    "id": 594226727,
    "state": "CANCELED",
    "date": "2018-09-12T21:27:25.241689",
    "operationAmount": {
      "amount": "67314.70",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Visa Platinum 1246377376343588",
    "to": "Счет 14211924144426031657"
  },
  {
    "id": 615064591,
    "state": "CANCELED",
    "date": "2018-10-14T08:21:33.419441",
    "operationAmount": {
      "amount": "77751.04",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 3928549031574026",
    "to": "Счет 84163357546688983493"
  },
  {
    "id": 147815167,
    "state": "EXECUTED",
    "date": "2018-01-26T15:40:13.413061",
    "operationAmount": {
      "amount": "50870.71",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на счет",
    "from": "Maestro 4598300720424501",
    "to": "Счет 43597928997568165086"
  },
  {
    "id": 518707726,
    "state": "EXECUTED",
    "date": "2018-11-29T07:18:23.941293",
    "operationAmount": {
      "amount": "3348.98",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "MasterCard 3152479541115065",
    "to": "Visa Gold 9447344650495960"
  }]


def test_read_file_json_successful_try():
    with patch('builtins.open', new_callable=mock_open, read_data=f'{test_data}'):
        assert read_file_json('testfile') == loads(test_data)


def test_read_file_json_no_type_list():
    with patch('builtins.open', new_callable=mock_open, read_data="""{"test": 1}"""):
        assert read_file_json('testfile') == []


def test_read_file_json_decode_error():
    with patch('builtins.open', new_callable=mock_open, read_data='test'):
        assert read_file_json('testfile') == []


def test_read_file_json_file_not_found():
    with patch('builtins.open', new_callable=mock_open) as mock_file:
        mock_file.side_effect = FileNotFoundError('File not found')
        assert read_file_json('testfile') == []


def test_process_bank_search():
    assert process_bank_search(test_list, 'Открытие') == [{
    "id": 863064926,
    "state": "EXECUTED",
    "date": "2019-12-08T22:46:21.935582",
    "operationAmount": {
      "amount": "41096.24",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Открытие вклада",
    "to": "Счет 90424923579946435907"
  }]

def test_process_bank_search_missing_request():
    assert process_bank_search(test_list, '1') == []


def test_process_bank_search_empty_request():
    assert process_bank_search(test_list, '') == test_list


def test_process_bank_operations():
    assert (process_bank_operations(test_list,
["Открытие вклада", "Перевод с карты на счет"]) == {'Открытие вклада': 1, 'Перевод с карты на счет': 2})


def test_process_bank_operations_empty_list():
    assert process_bank_operations(test_list, []) == {}


def test_process_bank_operations_missing_request():
    assert process_bank_operations(test_list, ['test']) == {}



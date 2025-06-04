from json import loads
from unittest.mock import patch, mock_open

from src.utils import read_file_json


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

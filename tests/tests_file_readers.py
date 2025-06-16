import csv
from unittest import mock
from unittest.mock import patch, mock_open, MagicMock

import pytest
from src.file_readers import read_xlsx_file,read_csv_file


@pytest.fixture()
def my_csv_file():
    return ['id;state;date;amount;currency_name;currency_code;from;to;description',
            '650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации']


def test_read_csv_success(my_csv_file):
    mock_file = MagicMock()
    mock_file.__enter__.return_value = mock_file

    mock_file.__iter__.return_value = iter(my_csv_file)

    with patch('builtins.open', return_value=mock_file) as mocked_open:
        result = read_csv_file('test.csv')

    mocked_open.assert_called_once_with('test.csv', encoding='utf-8')

    expected = [
    {
        'id': '650703',
        'state': 'EXECUTED',
        'date': '2023-09-05T11:30:32Z',
        'amount': '16210',
        'currency_name': 'Sol',
        'currency_code': 'PEN',
        'from': 'Счет 58803664561298323391',
        'to': 'Счет 39745660563456619397',
        'description': 'Перевод организации'
    }
]
    assert result == expected


def test_read_csv_file_not_found():
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = read_csv_file('missing.csv')

    assert result == 'Файл не найден'
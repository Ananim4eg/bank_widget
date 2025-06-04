import os

import requests
from dotenv import load_dotenv


def conversion_currency(transaction: dict) -> float:
    """
    Получает на вход словарь с данными о транзакции.
    Конвертирует валюту из USD и EUR в RUB и возвращает сумму транзакции в рублях
    """
    currency = transaction["operationAmount"]["currency"]["code"]
    amount: float = transaction["operationAmount"]["amount"]

    load_dotenv()

    if currency in ["USD", "EUR"]:

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

        headers = {"apikey": os.getenv("API_KEY")}

        response = requests.get(url, headers=headers).json()

        result: float = response["result"]
        if response.status_code == 200:
            return result

    return amount

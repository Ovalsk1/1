import os

import requests
from dotenv import load_dotenv

# Загрузим переменные окружения
load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")

BASE_URL = "https://api.apilayer.com/exchangerates_data/latest"
HEADERS = {"apikey": API_KEY}


def get_current_rate(from_currency: str, to_currency: str = "RUB") -> float:
    """
    Получает текущий курс обмена валюты.
    """
    params = {"base": from_currency, "symbols": to_currency}
    response = requests.get(BASE_URL, headers=HEADERS, params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get("rates", {}).get(to_currency)
    else:
        raise Exception(f"Ошибка при обращении к API: {response.text}")


def convert_to_rubles(amount: float, currency: str) -> float:
    """
    Конвертирует сумму из указанной валюты в рубли.
    """
    if currency == "RUB":
        return amount
    else:
        rate = get_current_rate(currency)
        return amount * rate


def process_transaction(transaction: dict) -> float:
    """
    Обрабатывает транзакцию и возвращает сумму в рублях.
    """
    amount = float(transaction.get("amount"))
    currency = transaction.get("currency", {}).get("code")

    # Конвертируем сумму в рубли
    converted_amount = convert_to_rubles(amount, currency)
    return converted_amount

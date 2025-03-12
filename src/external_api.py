import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found. Please check your .env file.")


def get_amount(transaction: dict) -> float:
    """Функция принимает на вход транзакцию, конвертирует сумму в рубли и возвращает сумму транзакции"""
    amount = transaction["operationAmount"]["amount"]
    code = transaction["operationAmount"]["currency"]["code"]

    if code != "RUB":
        response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}",
            headers={"apikey": API_KEY},
        )

        if response.status_code != 200:
            raise Exception(f"Error fetching data from API: {response.status_code} - {response.text}")

        result = response.json()
        return result["result"]
    else:
        return float(amount)

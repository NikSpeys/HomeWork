import json
import logging
import os

from src.external_api import get_amount

logger = logging.getLogger("utils")
file_handler = logging.FileHandler("../logs/utils.log", "a", encoding="utf8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def load_transactions_from_json(file_path: str) -> list[dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    logger.info("Принимаем путь до JSON-файла и возвращаяем данные в виде списка словарей")
    if not os.path.isfile(file_path):
        logger.error("Ошибка, файл не найден")
        return []

    logger.info("Открываем файл")
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            logger.error("Ошибка файла транзакций")
            return []

    if isinstance(data, list):
        logger.error("Ошибка, список транзакций пуст")
        return data
    else:
        logger.info("Создаём список словарей")
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    if trans["operationAmount"]["currency"]["code"] == currency:
        logger.info("Код транзакции валюты")
        amount = trans["operationAmount"]["amount"]
    else:
        logger.error("Конвертация валюты")
        amount = get_amount(trans)
    return amount


print(
    transaction_amount(
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    )
)

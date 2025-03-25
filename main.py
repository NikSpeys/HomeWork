from src.generators import  filter_by_currency
from src.processing import sort_by_date
from src.searching_transactions import search_transaction
from src.widget import get_date, mask_account_card
from src.transactions_csv_excel import read_transactions_csv, read_transactions_excel
from src.utils import load_transactions_from_json


def hello_user() -> list:
    """
    Выводит приветствие пользователя и запрашивает у него выбор файла для загрузки транзакций.
    """
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")

    dialogue_user = input(
        "1. Получить информацию о транзакциях из JSON-файла"
        "\n2. Получить информацию о транзакциях из CSV-файла"
        "\n3. Получить информацию о транзакциях из XLSX-файла"
        "\nВвод: "
    ).strip()
    while True:
        if dialogue_user == "1":
            print("Для обработки выбран JSON-файл.")
            return load_transactions_from_json("../data/operations.json")

        elif dialogue_user == "2":
            print("Для обработки выбран CSV-файл.")
            return read_transactions_csv("../data/transactions.csv")

        elif dialogue_user == "3":
            print("Для обработки выбран XLSX-файл.")
            return read_transactions_excel("../data/transactions_excel.xlsx")

        else:
            dialogue_user = input(
                "Выбран несуществующий формат. Попробуйте еще раз\nВвод: "
            ).strip()


def status_transactions(transactions: list) -> list:
    """
    Запрашивает у пользователя статус для фильтрации транзакций
    и выдаёт список транзакций с заданным статусом.
    """
    state_user = input(
        "Введите статус, по которому необходимо выполнить фильтрацию."
        "\nДоступные для фильтрации статусы: EXECUTED, CANCELED, PENDING"
        "\nВвод: "
    ).strip().upper()

    valid_states = {"EXECUTED", "CANCELED", "PENDING"}

    while state_user not in valid_states:
        print(f"Статус операции {state_user} недоступен.")
        state_user = input(
            "Введите статус, по которому необходимо выполнить фильтрацию."
            "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\nВвод: "
        ).upper()

    filtered_transactions = [x for x in transactions if x.get("state") == state_user]
    print(f"Операции отфильтрованы по статусу {state_user}")
    return filtered_transactions


def sort_transactions_date(file_list: list) -> list:
    """Функция для запроса у пользователя о необходимости сортировки по дате."""
    while True:
        sort_date = input("Отсортировать операции по дате? 'Да' или 'Нет'\nВвод: ").strip().lower()

        if sort_date == "да":
            reversing = input(
                "Отсортировать по возрастанию или по убыванию? (введите 'по возрастанию' или 'по убыванию')\nВвод: "
            ).strip().lower()

            if reversing == "по возрастанию":
                return sort_by_date(file_list, reverse=False)
            elif reversing == "по убыванию":
                return sort_by_date(file_list, reverse=True)
            else:
                print("Некорректный ввод. Пожалуйста, введите 'по возрастанию' или 'по убыванию'.")

        elif sort_date == "нет":
            return file_list

        else:
            print("Некорректный ввод. Пожалуйста, введите 'Да' или 'Нет'.")


def rub_transactions(transactions: list) -> list:
    """Функция для фильтрации списков транзакций по валюте"""
    while True:
        input_user_currency = input(
            "Выводить только рублевые транзакции? 'Да' или 'Нет'\nВвод: "
        ).strip().lower()
        if input_user_currency == "да":
            return list(filter_by_currency(transactions, "RUB"))
        elif input_user_currency == "нет":
            return transactions
        else:
            print("Некорректный ввод! Пожалуйста, введите 'Да' или 'Нет'.")


def filter_search_word(transactions: list) -> list:
    """Функция для поиска транзакций по определенному слову"""
    user_input_search = input(
        "Отфильтровать список транзакций по определенному слову в описании? 'Да' или 'Нет'\nВвод: "
    ).lower()
    if user_input_search == "да":
        string_to_search = input("Введите слово: ")
        data = search_transaction(transactions, string_to_search)
        return data
    else:
        return transactions


def result(file_list: list) -> None:
    """Функция для вывода результата"""
    if len(list(file_list)) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(file_list)}\n")

    for transaction in file_list:
        date = get_date(transaction.get("date"))

        try:
            mask_from = mask_account_card(transaction["from"])
            print(f"{date} {transaction['description']} {str(mask_from)} -> ", end="")
        except KeyError:
            print(f"{date} {transaction['description']} ", end="")
        except AttributeError:
            print(f"{date} {transaction['description']} ", end="")

        mask_to = mask_account_card(transaction["to"])
        try:
            amount = transaction["amount"]
        except KeyError:
            amount = transaction["operationAmount"]["amount"]
        try:
            currency = transaction["currency_name"]
        except KeyError:
            currency = transaction["operationAmount"]["currency"]["name"]
        print(f"{mask_to} Сумма: {amount} {currency}")


def main() -> None:
    hello = hello_user()
    status = status_transactions(hello)
    date = sort_transactions_date(status)
    transactions = rub_transactions(date)
    data = filter_search_word(transactions)
    result(data)


if __name__ == "__main__":
    main()
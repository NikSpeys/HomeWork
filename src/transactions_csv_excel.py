import pandas as pd


def read_transactions_csv(file_csv: str) -> list[dict]:
    """Функция чтения финансовых транзакций из CSV-файла"""
    try:
        csv_file_read = pd.read_csv(file_csv, sep=";")
        return csv_file_read.to_dict(orient="records")
    except FileNotFoundError:
        csv_file_read = []
        return csv_file_read


def read_transactions_excel(file_excel: str) -> list[dict]:
    """Функция чтения финансовых транзакций из Excel-файла"""
    try:
        excel_file_read = pd.read_excel(file_excel)
        return excel_file_read.to_dict(orient="records")
    except FileNotFoundError:
        excel_file_read = []
        return excel_file_read


print(read_transactions_csv("..//data/transactions.csv"))
print(read_transactions_excel("..//data/transactions_excel.xlsx"))

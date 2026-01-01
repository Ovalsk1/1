from pathlib import Path
import pandas as pd
import csv

def read_financial_transactions_from_csv(file_path: Path) -> list[dict]:
    """
    Функция для чтения CSV-файла и возврата списка словарей.
    """
    result = []
    with open(file_path, mode='r', newline='', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            result.append(row)
    return result


def read_financial_transactions_from_excel(excel_file_path: Path) -> list[dict]:
    """Функция для считывания финансовых операций из Excel."""
    df = pd.read_excel(excel_file_path)
    transactions = df.to_dict(orient="records")
    return transactions

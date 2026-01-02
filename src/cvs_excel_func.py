import csv
from pathlib import Path
import pandas as pd

data_dir = Path(__file__).parent.parent / "data"


def read_financial_transactions_from_csv(file_path: Path) -> list[dict]:
    """
    Функция для чтения CSV-файла и возврата списка словарей.
    """
    result = []
    with open(file_path, mode="r", newline="", encoding="utf-8-sig") as file:
        reader = csv.reader(file, delimiter=";")
        keys = next(reader)
        for row in reader:
            result.append(dict(zip(keys, row)))
    return result


def read_financial_transactions_from_excel(excel_file_path: Path) -> list[dict]:
    """Функция для считывания финансовых операций из Excel."""
    df = pd.read_excel(excel_file_path)
    transactions = df.to_dict(orient="records")
    return transactions

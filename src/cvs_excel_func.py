from pathlib import Path
import pandas as pd

def read_financial_transactions_from_csv(csv_file_path: Path) -> list[dict]:
    """Функция для считывания финансовых операций из CSV."""
    df = pd.read_csv(csv_file_path)
    transactions = df.to_dict(orient="records")
    return transactions


def read_financial_transactions_from_excel(excel_file_path: Path) -> list[dict]:
    """Функция для считывания финансовых операций из Excel."""
    df = pd.read_excel(excel_file_path)
    transactions = df.to_dict(orient="records")
    return transactions



import unittest
from unittest.mock import patch
import pandas as pd
from src.сsv_excel_func import read_financial_transactions_from_csv, read_financial_transactions_from_excel
from pathlib import Path

class TestFinancialTransactions(unittest.TestCase):

    @patch('pandas.read_csv')
    def test_read_financial_transactions_from_csv(self, mock_read_csv):
        # Подготавливаем моки
        mock_data = pd.DataFrame({
            'TransactionID': [1, 2, 3],
            'Amount': [100, 200, 300],
            'Date': ['2023-01-01', '2023-01-02', '2023-01-03']
        })
        mock_read_csv.return_value = mock_data

        # Вызываем функцию
        result = read_financial_transactions_from_csv(Path('mock_csv_file.csv'))

        # Проверяем результат
        expected_result = [
            {'TransactionID': 1, 'Amount': 100, 'Date': '2023-01-01'},
            {'TransactionID': 2, 'Amount': 200, 'Date': '2023-01-02'},
            {'TransactionID': 3, 'Amount': 300, 'Date': '2023-01-03'}
        ]
        self.assertEqual(result, expected_result)

    @patch('pandas.read_excel')
    def test_read_financial_transactions_from_excel(self, mock_read_excel):
        # Подготавливаем моки
        mock_data = pd.DataFrame({
            'TransactionID': [1, 2, 3],
            'Amount': [100, 200, 300],
            'Date': ['2023-01-01', '2023-01-02', '2023-01-03']
        })
        mock_read_excel.return_value = mock_data

        # Вызываем функцию
        result = read_financial_transactions_from_excel(Path('mock_excel_file.xlsx'))

        # Проверяем результат
        expected_result = [
            {'TransactionID': 1, 'Amount': 100, 'Date': '2023-01-01'},
            {'TransactionID': 2, 'Amount': 200, 'Date': '2023-01-02'},
            {'TransactionID': 3, 'Amount': 300, 'Date': '2023-01-03'}
        ]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
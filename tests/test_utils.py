import unittest
from pathlib import Path
from typing import Dict, List

from src.utils import load_financial_transactions

# Определяем корень проекта (два уровня выше текущего файла)
PROJECT_ROOT = Path(__file__).parent.parent


class TestLoadFinancialTransactions(unittest.TestCase):

    def setUp(self) -> None:
        """ Пути к тестовым файлам"""
        self.valid_json_file: Path = PROJECT_ROOT / "data" / "valid_operations.json"
        self.invalid_json_file: Path = PROJECT_ROOT / "data" / "invalid_operations.json"
        self.nonexistent_file: Path = PROJECT_ROOT / "data" / "nonexistent.json"

    def test_valid_json(self) -> None:
        """Тестируем загрузку из валидного JSON-файла."""
        result: List[Dict] = load_financial_transactions(str(self.valid_json_file))
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_invalid_json(self) -> None:
        """Тестируем некорректный JSON-файл."""
        result: List[Dict] = load_financial_transactions(str(self.invalid_json_file))
        self.assertEqual(result, [])

    def test_nonexistent_file(self) -> None:
        """Тестируем ситуацию, когда файл не найден."""
        result: List[Dict] = load_financial_transactions(str(self.nonexistent_file))
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import MagicMock, patch

from dotenv import load_dotenv

from src.external_api import convert_to_rubles, get_current_rate, process_transaction

# Загружаем переменные окружения
load_dotenv()


class TestExternalApiFunctions(unittest.TestCase):

    def setUp(self) -> None:
        """Предварительная подготовка данных"""
        self.transaction_usd = {"amount": "100.00", "currency": {"name": "US Dollar", "code": "USD"}}
        self.transaction_rub = {"amount": "100.00", "currency": {"name": "Russian Ruble", "code": "RUB"}}

    @patch("src.external_api.requests.get")
    def test_get_current_rate(self, mock_requests_get: MagicMock) -> None:
        """Готовим мок-ответ от API"""
        mock_response = MagicMock()
        mock_response.json.return_value = {"base": "USD", "rates": {"RUB": 80.0}}
        mock_response.status_code = 200  # Добавляем статус-код
        mock_requests_get.return_value = mock_response

        # Проверяем получение курса USD -> RUB
        rate = get_current_rate("USD")
        self.assertAlmostEqual(rate, 80.0)

    @patch("src.external_api.requests.get")
    def test_convert_to_rubles(self, mock_requests_get: MagicMock) -> None:
        """Готовим мок-ответ от API"""
        mock_response = MagicMock()
        mock_response.json.return_value = {"base": "USD", "rates": {"RUB": 80.0}}
        mock_response.status_code = 200  # Добавляем статус-код
        mock_requests_get.return_value = mock_response

        # Проверяем конвертацию из USD в RUB
        amount = convert_to_rubles(100.0, "USD")
        self.assertAlmostEqual(amount, 8000.0)

    @patch("src.external_api.requests.get")
    def test_process_transaction(self, mock_requests_get: MagicMock) -> None:
        """Готовим мок-ответ от API"""
        mock_response = MagicMock()
        mock_response.json.return_value = {"base": "USD", "rates": {"RUB": 80.0}}
        mock_response.status_code = 200  # Добавляем статус-код
        mock_requests_get.return_value = mock_response

        # Проверяем обработку транзакции в USD
        result = process_transaction(self.transaction_usd)
        self.assertAlmostEqual(result, 8000.0)

        # Проверяем обработку транзакции в RUB
        result = process_transaction(self.transaction_rub)
        self.assertAlmostEqual(result, 100.0)

    @patch("src.external_api.requests.get")
    def test_error_handling(self, mock_requests_get: MagicMock) -> None:
        """Готовим ошибку от API"""
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.json.return_value = {"error": "Internal Server Error"}
        mock_requests_get.return_value = mock_response

        # Проверяем обработку ошибки
        with self.assertRaises(Exception):
            get_current_rate("USD")


if __name__ == "__main__":
    unittest.main()

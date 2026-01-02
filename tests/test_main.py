import sys
import unittest
from unittest.mock import patch
from io import StringIO
from pathlib import Path
from src.main import main

data_dir = Path(__file__).parent.parent / "data"
cvs_excel_dir = Path(__file__).parent.parent / "cvs_excel"
class TestMainFunction(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None  # Чтобы видеть большие различия в выводе
        self.data_dir = data_dir


    def capture_console_output(self, user_inputs):
        # Каптим поток stdout
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        with patch('builtins.input', side_effect=user_inputs):
            main()
        console_output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        return console_output.strip()

    def test_full_workflow_json(self):
        # Подготовим пользовательский ввод для полного прохождения сценария
        user_inputs = [
            "1",               # Выбор загрузки из JSON
            "CANCELED",        # Фильтрация по статусу CANCELED
            "Да",              # Согласие на сортировку
            "По убыванию",     # По убыванию
            "Да",              # Только рублевые транзакции
            "Да",              # Поиск по описанию
            "Открытие",         # Ключевое слово для поиска
        ]

        expected_result = """Распечатываю итоговый список транзакций...

18.04.2019 Открытие вклада
Счет **4865
Сумма: 73778.48 руб.

Всего банковских операций в выборке: 1"""

        actual_output = self.capture_console_output(user_inputs)
        self.assertIn(expected_result, actual_output)

    def test_csv_file_processing(self):
        # Проверка загрузки из CSV и фильтрации по статусу
        user_inputs = [
            "2",                 # Выбор загрузки из CSV
            "PENDING",          # Фильтрация по статусу PENDING
            "Нет",               # Без сортировки по дате
            "Да",               # Фильтрация по валюте RUB
            "Нет",               # Нет фильтрации по описанию
        ]

        expected_result = """Распечатываю итоговый список транзакций...

25.02.2020 Перевод с карты на карту
Mastercard 4597 61** **** 2324 -> Visa 2648 49** **** 4307
Сумма: 17655 Ruble

07.06.2020 Перевод с карты на карту
Visa 6644 69** **** 6766 -> Mastercard 8548 96** **** 6541
Сумма: 12234 Ruble

19.02.2021 Перевод с карты на карту
Mastercard 9775 49** **** 9116 -> Discover 5944 50** **** 3459
Сумма: 12918 Ruble

08.02.2022 Перевод с карты на карту
Discover 6348 32** **** 5461 -> Mastercard 7325 94** **** 4710
Сумма: 15911 Ruble

05.10.2020 Открытие вклада
Счет **6195
Сумма: 31503 Ruble

06.02.2020 Перевод с карты на карту
Mastercard 7673 26** **** 9337 -> Discover 6961 58** **** 5561
Сумма: 12480 Ruble

11.04.2022 Перевод организации
Mastercard 5612 50** **** 7911 -> Счет **0384
Сумма: 11280 Ruble

20.06.2021 Перевод с карты на карту
American Express 2932 52** **** 4117 -> American Express 3633 64** **** 8444
Сумма: 19321 Ruble

09.06.2022 Перевод с карты на карту
Visa 4756 82** **** 5661 -> Discover 6499 54** **** 6238
Сумма: 30387 Ruble

Всего банковских операций в выборке: 9"""

        actual_output = self.capture_console_output(user_inputs)
        self.assertIn(expected_result, actual_output)

    def test_invalid_choice(self):
        # Проверка реакции на неверный выбор пункта меню
        user_inputs = [
            "5",                 # Некорректный выбор
        ]

        expected_result = """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
Ошибка: Неверный выбор пункта меню."""
        actual_output = self.capture_console_output(user_inputs)
        self.assertEqual(actual_output, expected_result)


if __name__ == '__main__':
    unittest.main()
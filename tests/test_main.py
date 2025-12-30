import unittest
from unittest.mock import patch

from src.main import ask_yes_or_no, display_menu, get_user_choice, main, prepare_data


class TestMainFunctions(unittest.TestCase):

    @patch("builtins.input")
    def test_display_menu(self, mock_input):
        mock_input.return_value = "1"
        result = display_menu()
        self.assertEqual(result, "1")

    def test_get_user_choice(self):
        # Проверка выбора статуса
        with patch("builtins.input", side_effect=["EXECUTED"]):
            choices = ["EXECUTED", "CANCELED", "PENDING"]
            result = get_user_choice(choices)
            self.assertEqual(result, "EXECUTED")

        # Проверка неправильного ввода
        with patch("builtins.input", side_effect=["INVALID", "EXECUTED"]):
            choices = ["EXECUTED", "CANCELED", "PENDING"]
            result = get_user_choice(choices)
            self.assertEqual(result, "EXECUTED")

    def test_ask_yes_or_no(self):
        # Положительный ответ
        with patch("builtins.input", return_value="да"):
            result = ask_yes_or_no("Вопрос?")
            self.assertTrue(result)

        # Отрицательный ответ
        with patch("builtins.input", return_value="нет"):
            result = ask_yes_or_no("Вопрос?")
            self.assertFalse(result)

    def test_prepare_data(self):
        # Проверка выбора первого пункта меню (загрузка из JSON)
        with patch("builtins.input", return_value="1"):
            result = prepare_data("1")
            self.assertIsInstance(result, list)

        # Проверка выбора третьего пункта меню (загрузка из Excel)
        with patch("builtins.input", return_value="3"):
            result = prepare_data("3")
            self.assertIsInstance(result, list)

    @patch("builtins.input")
    def test_main_function(self, mock_input):
        # Эмулируем стандартный поток действий
        mock_input.side_effect = ["1", "EXECUTED", "да", "по возрастанию", "да", "руб.", "да", "перевод"]
        main()


if __name__ == "__main__":
    unittest.main()

import unittest

from src.bank_utils import count_bank_operations, process_bank_search


class TestBankSearchFunction(unittest.TestCase):

    def setUp_(self):
        self.data = [
            {"id": 1, "description": "Оплата телефона МТС"},
            {"id": 2, "description": "Покупка еды в магазине"},
            {"id": 3, "description": "Автоплатеж ЖКХ"},
            {"id": 4, "description": "Перевод другу"},
            {"id": 5, "description": "Абонентская плата за интернет"},
        ]

    def test_exact_match(self):
        """Тестирование точного совпадения"""
        result = process_bank_search(self.data, "телефон")
        self.assertEqual(len(result), 1)
        self.assertIn({"id": 1, "description": "Оплата телефона МТС"}, result)

    def test_case_insensitive(self):
        """Тестирование поиска без учета регистра"""
        result = process_bank_search(self.data, "АВТОПЛАТЕЖ")
        self.assertEqual(len(result), 1)
        self.assertIn({"id": 3, "description": "Автоплатеж ЖКХ"}, result)

    def test_multiple_matches(self):
        """Тестирование множественных совпадений"""
        result = process_bank_search(self.data, "(телефон)|(интернет)")
        self.assertEqual(len(result), 2)
        self.assertIn({"id": 1, "description": "Оплата телефона МТС"}, result)
        self.assertIn({"id": 5, "description": "Абонентская плата за интернет"}, result)

    def test_no_matches(self):
        """Тестирование, когда нет совпадений"""
        result = process_bank_search(self.data, "авиабилеты")
        self.assertEqual(result, [])

    def setUp(self):
        self.data = [
            {"id": 1, "description": "Оплата телефона МТС"},
            {"id": 2, "description": "Покупка в магазине"},
            {"id": 3, "description": "Автоплатеж ЖКХ"},
            {"id": 4, "description": "Перевод другу"},
            {"id": 5, "description": "Абонентская плата за интернет"},
        ]

    def test_simple_categories(self):
        """Тестирование простого распределения по категориям"""
        categories = ["телефон", "Покупка", "Интернет"]
        result = count_bank_operations(self.data, categories)
        expected = {"телефон": 1, "Покупка": 1, "Интернет": 1}
        self.assertEqual(result, expected)

    def test_full_categories(self):
        """Тестирование полного набора категорий"""
        categories = ["Телефон", "Покупка", "ЖКХ", "Перевод", "Интернет"]
        result = count_bank_operations(self.data, categories)
        expected = {"Телефон": 1, "Покупка": 1, "ЖКХ": 1, "Перевод": 1, "Интернет": 1}
        self.assertEqual(result, expected)

    def test_single_category(self):
        """Тестирование единственной категории"""
        categories = ["телефон"]
        result = count_bank_operations(self.data, categories)
        expected = {"телефон": 1}
        self.assertEqual(result, expected)

    def test_empty_categories(self):
        """Тестирование пустого списка категорий"""
        categories = []
        result = count_bank_operations(self.data, categories)
        expected = {}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

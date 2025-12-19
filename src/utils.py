import json
from pathlib import Path
from typing import Dict, List


def load_financial_transactions(json_file_path: str) -> List[Dict]:
    """Конвертирует данные из формата .json в список."""
    try:
        # Открываем файл и читаем его содержимое
        with open(json_file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Проверяем, что данные представляют собой список
        if isinstance(data, list):
            return data
        else:
            return []

    except (json.JSONDecodeError, FileNotFoundError):
        # Невозможно загрузить JSON или файл не найден
        return []


project_root = Path(__file__).parent.parent  # двигаемся на два уровня вверх (отдельно от *.py файла)
file_path = project_root / "data" / "operations.json"

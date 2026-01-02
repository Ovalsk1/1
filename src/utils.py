import json
import logging
import os
from pathlib import Path
from typing import Dict, List

# Относительный путь к папке "logs"
logs_folder = Path(__file__).parent.parent / "logs"

# Настраиваем логирование
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования на DEBUG

# Создаем файловый хэндлер для DEBUG и выше
file_handler = logging.FileHandler(os.path.join(logs_folder, "utils_log.log"), mode="w")
file_handler.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования для хэндлера

# Создаем форматтер
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавляем хэндлер к логгеру
logger.addHandler(file_handler)

# Создаем файловый хэндлер для ошибок (уровень ERROR и выше)
error_handler = logging.FileHandler(os.path.join(logs_folder, "errors_utils_log.log"), mode="w")
error_handler.setLevel(logging.ERROR)  # Устанавливаем уровень логирования для хэндлера

# Создаем форматтер для ошибок
error_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
error_handler.setFormatter(error_formatter)

# Добавляем хэндлер для ошибок к логгеру
logger.addHandler(error_handler)


def load_financial_transactions(json_file_path: Path) -> List[Dict]:
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

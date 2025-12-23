import logging
from pathlib import Path

# Относительный путь к папке "logs"
logs_folder = Path(__file__).parent.parent / "logs"

# Настраиваем логирование
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Устанавливаем уровень логирования на INFO

# Создаем файловый хэндлер для INFO и выше
file_handler = logging.FileHandler(logs_folder / "masks_log.log", mode="w")
file_handler.setLevel(logging.INFO)  # Устанавливаем уровень логирования для хэндлера

# Создаем форматтер
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)

# Добавляем хэндлер к логгеру
logger.addHandler(file_handler)

# Создаем файловый хэндлер для ошибок (уровень ERROR и выше)
error_handler = logging.FileHandler(logs_folder / "masks_errors.log", mode="w")
error_handler.setLevel(logging.ERROR)  # Устанавливаем уровень логирования для хэндлера

# Создаем форматтер для ошибок
error_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
error_handler.setFormatter(error_formatter)

# Добавляем хэндлер для ошибок к логгеру
logger.addHandler(error_handler)


def get_mask_card_number(card_number: int) -> str:
    """Функция которая принимает номер карты и возвращает маску номера"""
    card_number_str = str(card_number)
    part1 = card_number_str[:4]  # Первая часть номера
    part2 = card_number_str[4:6]  # Вторая часть номера
    masked_part = "**"  # Третья часть номера
    part4 = card_number_str[-4:]  # Четвёртая часть номера
    result = f"{part1} {part2}{masked_part} **** {part4}"  # Собираем всё вместе с пробелами
    logger.info(f"Маска номера карты: {result}")
    return result


def get_mask_account(account_number: int) -> str:
    """Функция которая принимает номер счета и возвращает маску номера"""
    account_number_str = str(account_number)
    mask = "**"  # Скрытая часть номера
    part_account_number = account_number_str[-4:]  # Оставшаяся часть номера
    result = f"{mask}{part_account_number}"  # Собираем вместе
    logger.info(f"Маска номера счета: {result}")
    return result

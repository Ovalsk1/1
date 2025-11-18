def get_mask_card_number(card_number: int) -> str:
    """Функция которая принимает номер карты и возвращает маску номера"""
    card_number_str = str(card_number)
    part1 = card_number_str[:4]  # Первая часть номера
    part2 = card_number_str[4:6]  # Вторая часть номера
    masked_part = "**"  # Третья часть номера
    part4 = card_number_str[-4:]  # Четвёртая часть номера
    return f"{part1} {part2}{masked_part} **** {part4}"  # Собираем всё вместе с пробелами


def get_mask_account(account_number: int) -> str:
    """Функция которая принимает номер счета и возвращает маску номера"""
    account_number_str = str(account_number)
    mask = "**"  # Скрытая часть номера
    part_account_number = account_number_str[-4:]  # Оставшаяся часть номера
    return f"{mask}{part_account_number}"  # Собираем вместе




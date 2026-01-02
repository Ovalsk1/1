from datetime import datetime


def mask_account_card(account_string: str) -> str:
    """Принимает на вход строку с названием и номером, используя функции из masks выводит
    замаскированный номер карты или счета"""
    try:
        parts = account_string.split(
            " ",
        )
        name = parts[0:-1]
        type_name = " ".join(name)
        number = int(parts[-1])
        if type_name == "Счет":
            from src.masks import get_mask_account

            account_number = get_mask_account(number)
            return f"{type_name} {account_number}"
        else:
            from src.masks import get_mask_card_number

            card_number = get_mask_card_number(number)
            return f"{type_name} {card_number}"
    except AttributeError:
        return ""


def get_date(date: str) -> str:
    """Выводит дату введенную пользователем"""
    # Парсим дату из ISO-формата в объект datetime
    dt_object = datetime.fromisoformat(date)

    # Преобразовываем дату в нужный формат (ДД.ММ.ГГГГ)
    formatted_date = dt_object.strftime("%d.%m.%Y")

    return formatted_date

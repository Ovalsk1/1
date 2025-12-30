from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.utils import load_financial_transactions
from src.сsv_excel_func import read_financial_transactions_from_csv, read_financial_transactions_from_excel


def display_menu() -> str:
    """Показывает меню выбора источника данных и возвращает выбор пользователя."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1) Получить информацию о транзакциях из JSON-файла")
    print("2) Получить информацию о транзакциях из CSV-файла")
    print("3) Получить информацию о транзакциях из XLSX-файла")
    choice = input("Ваш выбор: ")
    return choice.strip()


def get_user_choice(options: list[str]) -> str:
    """Функция запрашивает у пользователя выбор из доступных опций и возвращает выбранный статус."""
    while True:
        user_input = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: {}\n".format(", ".join(options))
        ).upper()
        if user_input in options:
            return user_input
        else:
            print(f'Статус операции "{user_input}" недоступен.')


def ask_yes_or_no(question: str) -> bool:
    """Функция запрашивает подтверждение у пользователя (Да/Нет) и возвращает True или False."""
    answer = input(question + " (Да/Нет): ").strip().lower()
    return answer == "да"


def prepare_data(choice: str) -> list[dict]:
    """Функция загружает данные в зависимости от выбранного пользователем формата файла."""
    if choice == "1":
        return load_financial_transactions("data/bank_transactions.json")
    elif choice == "2":
        return read_financial_transactions_from_csv("data/bank_transactions.csv")
    elif choice == "3":
        return read_financial_transactions_from_excel("data/bank_transactions.xlsx")
    else:
        raise ValueError("Неправильный выбор источника данных.")


def main():
    # Показываем меню и получаем выбор пользователя
    choice = display_menu()

    # Загружаем данные в зависимости от выбора пользователя
    try:
        operations = prepare_data(choice)
    except Exception as e:
        print(f"Произошла ошибка при обработке файла: {e}")
        return

    # Выбор статуса операции
    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    state = get_user_choice(available_statuses)
    print(f'Операции отфильтрованы по статусу "{state}".')

    # Фильтруем операции по выбранному статусу
    filtered_operations = filter_by_state(operations, state)

    # Дополнительные фильтры
    if ask_yes_or_no("Отсортировать операции по дате?"):
        sort_order = input("Отсортировать по возрастанию или по убыванию?\n").strip().lower()
        if sort_order == "по возрастанию":
            filtered_operations = sort_by_date(filtered_operations, reverse=True)
        elif sort_order == "по убыванию":
            filtered_operations = sort_by_date(filtered_operations, reverse=False)
        else:
            print("Неверный ввод. Данные останутся неотсортированными.")

    if ask_yes_or_no("Выводить только рублевые транзакции?"):
        filtered_operations = list(filter_by_currency(filtered_operations))  # Преобразуем в список

    if ask_yes_or_no("Отфильтровать список транзакций по определенному слову в описании?"):
        keyword = input("Введите слово для поиска в описании: ").strip()
        filtered_operations = list(transaction_descriptions(filtered_operations, keyword))  # Преобразуем в список

    # Вывод итогового списка операций
    if filtered_operations:
        print("Распечатываю итоговый список транзакций...")
        for idx, op in enumerate(filtered_operations):
            print(f"{op['date']} {op['description']}")
            print(f"{op['from']} -> {op['to']}")
            print(f"Сумма: {op['amount']} {op['currency']}\n")
        print(f"Всего банковских операций в выборке: {len(filtered_operations)}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()

from pathlib import Path
from src.bank_utils import process_bank_search
from src.cvs_excel_func import read_financial_transactions_from_csv, read_financial_transactions_from_excel
from src.generators import filter_by_currency, filter_by_currency_not_json
from src.processing import filter_by_state, sort_by_date
from src.utils import load_financial_transactions
from src.widget import get_date, mask_account_card


def main():
    # Приветствие пользователя и предложение выбрать источник данных
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    # Чтение выбора пользователя
    choice = input("Ваш выбор: ").strip()

    # Определение пути к данным
    data_dir = Path(__file__).parent.parent / "data"

    # Загрузка данных в зависимости от выбора пользователя
    try:
        if choice == "1":
            operations = load_financial_transactions(data_dir / "bank_transactions.json")
            print("Для обработки выбран JSON-файл.")
        elif choice == "2":
            operations = read_financial_transactions_from_csv(data_dir / "bank_transactions.csv")
            print("Для обработки выбран CSV-файл.")
        elif choice == "3":
            operations = read_financial_transactions_from_excel(data_dir / "bank_transactions.xlsx")
            print("Для обработки выбран XLSX-файл.")
        else:
            print("Ошибка: Неверный выбор пункта меню.")
            return
    except Exception as e:
        print(f"Ошибка при загрузке данных: {e}.")
        return

    # Выбор статуса операций
    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: {}\n".format(", ".join(available_statuses))
        ).upper()
        if status in available_statuses:
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    # Фильтрация операций по выбранному статусу
    filtered_operations = filter_by_state(operations, status)
    print(f'Операции отфильтрованы по статусу "{status}".')

    # Дополнительные фильтры и сортировка
    if input("Отсортировать операции по дате? (Да/Нет): ").strip().lower() == "да":
        sort_order = (
            input("Отсортировать по возрастанию или по убыванию? (По возрастанию/По убыванию): ").strip().lower()
        )
        if sort_order == "по возрастанию":
            filtered_operations = sort_by_date(filtered_operations, reverse=False)
        elif sort_order == "по убыванию":
            filtered_operations = sort_by_date(filtered_operations, reverse=True)
        else:
            print("Неверный ввод. Данные останутся неотсортированными.")

    # Фильтрация по валюте
    if input("Выводить только рублевые транзакции? (Да/Нет): ").strip().lower() == "да":
        if choice == "1":
            filtered_operations = list(filter_by_currency(filtered_operations, currency="RUB"))
        else:
            filtered_operations = list(filter_by_currency_not_json(filtered_operations, currency="RUB"))

    # Фильтрация по описанию
    if input("Отфильтровать список транзакций по определенному слову в описании? (Да/Нет): ").strip().lower() == "да":
        keyword = input("Введите слово для поиска в описании: ").strip()
        filtered_operations = process_bank_search(filtered_operations, keyword)

    # Вывод итогового списка операций
    if filtered_operations:
        print("\nРаспечатываю итоговый список транзакций...\n")
        for idx, op in enumerate(filtered_operations):
            # Безопасный доступ к полям с указанием дефолтных значений
            date = op.get("date", "")
            description = op.get("description", "Описание отсутствует")
            from_field = op.get("from", "")
            to_field = op.get("to", "Получатель неизвестен")
            if choice == "1":
                amount = op.get("operationAmount", {}).get("amount", "Сумма неизвестна")
                currency = op.get("operationAmount", {}).get("currency", {}).get("name", "Валюта неизвестна")
            else:
                amount = op.get("amount", "Сумма неизвестна")
                currency = op.get("currency_name", "Валюта неизвестна")

            # Применение масок номеров счета или карты
            pars_date = get_date(date)
            mask_to_field = mask_account_card(to_field)

            # Разбиение операций по 'Открытие вклада' и остальным
            if from_field == "" or type(from_field) is float:
                print(f"{pars_date} {description}")
                print(f"{mask_to_field}")
                print(f"Сумма: {amount} {currency}\n")
            else:
                from_field = mask_account_card(from_field)
                print(f"{pars_date} {description}")
                print(f"{from_field} -> {mask_to_field}")
                print(f"Сумма: {amount} {currency}\n")

        print(f"Всего банковских операций в выборке: {len(filtered_operations)}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")


if __name__ == "__main__":
    main()

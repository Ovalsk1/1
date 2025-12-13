import pytest

from src.decorators import log  # Импортируем декоратор из вашего модуля


# Тест на успешное выполнение функции (при логировании в файл)
def test_log_success_in_file(tmpdir):
    logfile = tmpdir.join("test.log")

    @log(filename=str(logfile))
    def add(a, b):
        return a + b

    # Выполняем функцию
    result = add(1, 2)

    # Проверяем результат
    assert result == 3

    # Проверяем, что логи записались в файл
    with open(logfile, "r") as file:
        content = file.read()
        assert "add ok" in content


# Тест на обработку ошибки (при логировании в файл)
def test_log_error_in_file(tmpdir):
    logfile = tmpdir.join("test.log")

    @log(filename=str(logfile))
    def divide(a, b):
        return a / b

    # Выполняем функцию с исключением
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    # Проверяем, что ошибка записалась в файл
    with open(logfile, "r") as file:
        content = file.read()
        assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in content


# Тест на успешное выполнение функции (при логировании в консоль)
def test_log_success_in_console(capsys):
    @log()
    def add(a, b):
        return a + b

    # Выполняем функцию
    result = add(1, 2)

    # Проверяем результат
    assert result == 3

    # Захватываем вывод в консоль
    captured = capsys.readouterr()

    # Проверяем, что логи корректно выведены в консоль
    stdout = captured.out
    assert "add ok" in stdout


# Тест на обработку ошибки (при логировании в консоль)
def test_log_error_in_console(capsys):
    @log()
    def divide(a, b):
        return a / b

    # Выполняем функцию с исключением
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    # Захватываем вывод в консоль
    captured = capsys.readouterr()

    # Проверяем, что ошибка корректно выведена в консоль
    stderr = captured.err
    assert "divide error: ZeroDivisionError. Inputs: (1, 0), {}" in stderr

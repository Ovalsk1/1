import functools
import logging
from typing import Any, Callable, Optional

# Настройка базового логера
logging.basicConfig(level=logging.INFO, format="%(message)s")


def log(filename: Optional[str] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger = logging.getLogger(__name__)
            handler = None
            # Настройка файлового хэндлера, если filename задан
            if filename:
                file_handler = logging.FileHandler(filename)
                file_handler.setFormatter(logging.Formatter("%(message)s"))
                logger.addHandler(file_handler)
                handler = file_handler
            try:
                # Выполнение функции
                result = func(*args, **kwargs)
                # Логируем успешное завершение
                logger.info(f"{func.__name__} ok")
                return result
            except Exception as err:
                # Логируем ошибку
                logger.error(f"{func.__name__} error: {err.__class__.__name__}. Inputs: {args}, {kwargs}")
                raise
            finally:
                # Освобождаем хэндлер, если использовался файл
                if handler:
                    logger.removeHandler(handler)

        return wrapper

    return decorator

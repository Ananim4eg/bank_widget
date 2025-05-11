from datetime import datetime
from functools import wraps
from os import getcwd
from os.path import dirname
from typing import Any, Callable


def log(filename: str = " ") -> Any:
    """Декоратор для логирования работы функций"""
    def decorator(func: Callable) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            full_path = dirname(getcwd()) + "\\"
            start_time = datetime.now()
            try:
                result = func(*args, **kwargs)
                if filename != " ":
                    with open(f"{full_path + filename}", "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} ok\n\n")
                return result
            except Exception as e:
                if filename != " ":
                    with open(f"{full_path + filename}", "a", encoding="UTF-8") as file:
                        file.write(f"{func.__name__} error: {e}. Input: {args}, {kwargs}\n\n")
                    return f"Ошибка {e}"
                else:
                    return f"Ошибка {e}"
            finally:
                stop_time = datetime.now()
                working_time = stop_time - start_time

        return wrapper

    return decorator

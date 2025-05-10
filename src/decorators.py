from time import time
from functools import wraps


def decorator_with_args(filename: str = " "):
    def log(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time()
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as e:
                return f"Ошибка {e}"
            finally:
                stop_time = time()
                working_time = stop_time - start_time
        return wrapper
    return log

@decorator_with_args("1")
def example(a, b):
    return a * b


print(example("2", "2"))
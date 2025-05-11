from typing import Any

from src.decorators import log


def test_log(capsys: Any) -> None:

    @log(" ")
    def positive_example() -> str:
        return "Hello world"

    print(positive_example())

    captured = capsys.readouterr()
    assert captured.out == "Hello world\n"

    @log()
    def err_example() -> None:
        raise ValueError("Error this operation")

    print(err_example())

    err, out = capsys.readouterr()
    assert out == ""
    assert err == "Ошибка Error this operation\n"

    @log("mylog.txt")
    def write_log_in_file_positive_example(a: int, b: int) -> int:
        return a * b

    assert write_log_in_file_positive_example(2, 3) == 6

    @log("mylog.txt")
    def write_log_in_file_fail_example(a: int, b: int) -> int:
        if not (a * b):
            return a * b
        raise Exception("An error occurred during execution")

    print(write_log_in_file_fail_example(2, 7))

    err, out = capsys.readouterr()
    assert out == ""
    assert err == "Ошибка An error occurred during execution\n"

import pytest

from src.decorators import log


def test_log():
    @log(filename="my_log.txt")
    def addition(x, y):
        return x + y

    result_addition = addition(1, 2)
    assert (
        f"Функция my_function ок. Результат: {result_addition}"
        == "Функция my_function ок. Результат: 3"
    )

    def subtraction(x, y):
        return x - y

    result_subtraction = subtraction(2, 1)
    assert (
        f"Функция my_function ок. Результат: {result_subtraction}"
        == "Функция my_function ок. Результат: 1"
    )

    def division_zero(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        division_zero(2, 0)


@log()
def faulty_function(x, y):
    return x / y


def test_faulty_function_logs_error(capsys):
    faulty_function(1, 0)
    captured = capsys.readouterr()
    assert "faulty_function error: division by zero" in captured.out

import time


def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):

            try:
                time1 = time.time()
                time2 = time.time()
                result = func(*args, **kwargs)
                name_func = func.__name__
                good_line = f"Начало: {time1} \nФункция: {name_func} ок. Результат: {result} \nКонец: {time2} \n\n"

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(good_line)
                    return result
                else:
                    print(f"{name_func} ок. Результат: {result}")

            except Exception as ex:
                name_func = func.__name__
                error_line = f"{name_func} error: {ex}. Inputs: {args}, {kwargs}"
                result = None

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_line)
                    return error_line
                else:
                    print(error_line)

            except ZeroDivisionError as ze:
                name_func = func.__name__
                error_line = f"{name_func} error: {ze}. Inputs: {args}, {kwargs}"
                result = None

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(error_line)
                    return error_line
                else:
                    print(error_line)

            return result
        return wrapper

    return decorator

"""
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y

my_function(4, 0)
"""
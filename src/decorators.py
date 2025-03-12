from functools import wraps


def log(filename=None):
    """
    Декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    """

    def decorator(my_func):
        @wraps(my_func)
        def wrapper(*args, **kwargs):
            if not filename:
                print(f"{my_func.__name__} started")
                try:
                    result = my_func(*args, **kwargs)
                    print(f"{my_func.__name__} ok")
                    print(f"{my_func.__name__} finished")
                    return result
                except Exception as e:
                    print(f"{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}")
                    raise
            else:
                try:
                    result = my_func(*args, **kwargs)
                    with open(filename, "a+") as file:
                        file.write(f"{my_func.__name__} ok\n")
                    return result
                except Exception as e:
                    with open(filename, "a+") as file:
                        file.write(f"{my_func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                    raise

        return wrapper

    return decorator

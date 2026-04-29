import functools
import time


def measure_time(times=5):
    """
    Декоратор-фабрика для измерения среднего времени выполнения функции.

    Выполняет оборачиваемую функцию `times` раз, измеряет время каждого вызова
    и выводит среднее время выполнения.

    Параметры:
        times (int): количество повторных вызовов функции (по умолчанию 5).

    Возвращает:
        callable: декоратор, который оборачивает функцию и возвращает
        результат её последнего выполнения.

    Примечание:
        Использует time.time(), возможна погрешность измерений.
    """

    def function_decorator(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            total_time = 0
            result = None


            for _ in range(times):
                start = time.time()
                result = func(*args, **kwargs)
                total_time += time.time() - start


            mid_time = total_time / times

            print(f"Average function execution time over {times} calls: {mid_time:.2f} seconds\n"
                  f"Function result: ", end="")

            return result
        return wrapper
    return function_decorator



@measure_time(5)
def compute():
    total = 0
    for i in range(10_000_000):
        total +=i
    return total


print(compute())
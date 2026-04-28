from datetime import datetime

def make_rounder(degree: int):
    """
    Takes the degree of rounding and returns round function
    :param degree: the degree of rounding
    :return: Returns round function
    """
    def rounder(num: float):
        """
        Rounds number to some degree
        :param num: number to round
        :return: result of rounding
        """
        return round(num, degree)
    return rounder

round2 = make_rounder(2)
round0 = make_rounder(0)

print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))


#-----------------------------------------------------------------------------------------------------------------------


def make_logger():
    """
    An outer closure function within which a list of logs is created.
    :return: Returns the inner closure function.
    """
    events = []

    def logger(text=None):
        """
        An inner closure function that takes text for logging. Returns a list of logs.
        :param text: Text for logging
        :return: A list populated with logs
        """
        if text:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            events.append(f"{text}: {now}")
        return events

    return logger

log = make_logger()

log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")

for event in log():
    print(event)


#-----------------------------------------------------------------------------------------------------------------------

def frame(func):
    """
    A decorator function that accepts a function and passes it to an inner function.
    :param func: The function to be wrapped
    :return: Returns a wrapper function.
    """
    def wrapper():
        """
        The decorator's inner function wraps the target function between two prints.
        :return: None
        """
        print("-"*50)
        func()
        print("-" * 50)

    return wrapper


@frame
def say_hello():
    """
    Тестовая функция
    :return:
    """
    print("Привет, игрок!")


say_hello()


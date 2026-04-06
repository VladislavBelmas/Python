dividend = "345"
divider = "5a"


def divide (div1:str|int|float , div2:str|int|float) -> str|float:
    """
    Returns the result of dividing two numbers or an error.


    :param div1: dividend (what we divide)
    :param div2: divider (what do we divide into)
    :return: division result
    """

    import logging
    logging.basicConfig(filename='errors.log', level=logging.ERROR, format="%(asctime)s) - %(levelname)s - "
                                                     "%(filename)s - %(lineno)s - %(message)s")
    try:
        result = int(div1) / int(div2)

    except ValueError:
        result = "Ошибка: Введено некорректное число."
        logging.error(result)

    except ZeroDivisionError:
        result = "Ошибка: Нельзя делить на ноль."
        logging.error(result)

    return result


print(divide(dividend, divider))




    :param div1: dividend (what we divide)
    :param div2: divider (what do we divide into)
    :return: division result
    """

    import logging
    logging.basicConfig(filename='errors.log', level=logging.ERROR, format="%(asctime)s) - %(levelname)s - "
                                                     "%(filename)s - %(lineno)s - %(message)s")

    if not div1.isnumeric() or not div2.isnumeric():

        excep = "Ошибка: Введено некорректное число."
        raise ValueError(excep)
        logging.error(excp)

    if int(div2) == 0:

        excep = "Ошибка: Нельзя делить на ноль."
        raise ZeroDivisionError(excep)
        logging.error(excp)

    result = int(div1) / int(div2)
    return result


print(divide2(dividend, divider))
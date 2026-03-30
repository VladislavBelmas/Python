dividend = "345"
divider = "5a"


def divide (div1:str|int|float , div2:str|int|float) -> str|float:
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




num = 43197


def num_sum(i:int|list[int], acc = 0) -> int:
    """
    Returns summary for any int or list[int] value

    :param i: value to summary
    :param acc: accumulator for summary, don't use if don't need it
    :return: summary for value in first param
    """


    if not isinstance(i, list):
        i = list(map(int, str(i)))

    if not i:
        return acc


    return num_sum(i, i.pop() + acc)


print(num_sum(num))

#-----------------------------------------------------------------------------------------------------------------------

nested_numbers = [1, [2, 3], [4, [5, 6]], 7]


def flatten(lst:list) -> list:
    """
    Returns recreated list without sublists in

    :param lst: value to clean
    :return: list without sublists in
    """

    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))

        else:
            result.append(item)

    return result



def num_sum_inlist(i:list[int], acc = 0) -> int:
    """
    Uses a third-party function (flatten()) to unpack the nested elements in the list
    and returns the sum of all the numbers within the list


    :param i: list of numbers
    :param acc: start value for summary
    :return: sum of all numbers in list
    """

    i = flatten(i)

    if not i:
        return acc


    return num_sum_inlist(i, i.pop() + acc)

print(num_sum_inlist(nested_numbers))


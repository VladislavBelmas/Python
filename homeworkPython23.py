from typing import Any

data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]

def to_str(lst: list[Any]) -> str:
    '''

    Creates a string representation of the data

    :param lst: list of any data
    :return: string format of data
    '''

    return ' | '.join(str(item) for item in lst)


print(to_str(data))

#-----------------------------------------------------------------------------------------------------------------------

data = [

    {"name": "Alice", "scores": [10, 20, 30]},

    {"name": "Bob", "scores": [5, 15, 25]},

    {"name": "Charlie", "scores": [7, 17, 27]}

]


def score_sum(obj: list[dict]) -> int:
    '''

    Counts all scores in a list

    :param obj: user's score list
    :return: summary of scores
    '''

    result = 0
    for item in obj:
        result += sum(item['scores'])

    return result


print(score_sum(data))
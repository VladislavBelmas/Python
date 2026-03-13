def is_simple(n):
    if (n == 2 or n == 3) or (n % 2 and n % 3):
        return True

    return False

print(is_simple(17))

#-----------------------------------------------------------------------------------------------------------------------

def filter_numbers(num_type, *args):
    if num_type == 'even':
        num_is_even = True

    elif num_type == 'odd':
        num_is_even = False

    else:
        return 'Допускаются только фильтры "odd" или "even"'

    result = []

    for num in args:
        if num_is_even:

            if num % 2 == 0 or num == 0:
                result.append(num)

        else:
            if num % 2:
                result.append(num)

    return result


print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))

#-----------------------------------------------------------------------------------------------------------------------

def merge_dicts(*args):
    result = {}

    for diction in args:
        if not isinstance(diction, dict):
            return "Передан объект не являющийся словарем"

        for key, value in diction.items():
            result[key] = value

    return result


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
dict4 = {1}

print(merge_dicts(dict1, dict2, dict3, dict4))
print(merge_dicts(dict1, dict2, dict3))



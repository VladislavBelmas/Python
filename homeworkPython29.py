def Fibo_gen():
    """
    The function infinitely generates Fibonacci numbers


    :return: Returns the next Fibonacci number in order
    """

    a = 0
    b = 1
    while True:
        yield a
        b, a = a, b + a


for i in Fibo_gen():
    if i > 700:
        break
    print(i)

print("-"*80)
#-----------------------------------------------------------------------------------------------------------------------

data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

def uniq_nums(nums: list[int]):
    """
    Selects unique numbers from a list

    :param nums: list of numbers
    :return: Returns the next unique number in order
    """

    if not isinstance(nums, list):
        raise TypeError("Must be a list")


    old = set()
    for num in nums:
        if not isinstance(num, int):
            raise TypeError("Must be an int")

        if num not in old:
            yield num
            old.add(num)


for x in uniq_nums(data):
    print(x)
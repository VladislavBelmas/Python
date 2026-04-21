def Fibo_gen():
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

def uniq(nums):
    old = set()
    for num in nums:
        if num not in old:
            yield num
            old.add(num)


for x in uniq(data):
    print(x)
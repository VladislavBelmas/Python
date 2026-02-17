numbers = (3, 7, 2, 8, 5, 10, 1)
new_tuple = []

for i in range(len(numbers)):
    for j in range(i):
        if numbers[i] < numbers[j]:
            break
    else:
        new_tuple.append(numbers[i])

print(tuple(new_tuple))


numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
used_numbers = []
indexes = []
for number in numbers:
    if numbers.count(number) > 1 and number not in used_numbers:
        indexes.append(numbers.index(number))
        for i in range(numbers.count(number) - 1):
            indexes.append(numbers.index(number, indexes[-1] + 1))
        print(f'Индексы элемента {number}: {indexes}')
        indexes = []
    used_numbers.append(number)



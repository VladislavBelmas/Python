strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
new_strings = []

for string in strings:
    previous_item = '0'
    for item in reversed(string):
        if item.isdigit() and not previous_item.isdigit():
            break
        previous_item = item
    else:
        new_strings.append(string)

print("Строки с цифрами только в конце:", new_strings)


#-----------------------------------------------------------------------------------------------------------------------


numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
user_input = 3#int(input("Enter a number: "))

for number in numbers[:]:
    if number % user_input == 0:
        numbers.remove(number)

print("Список без кратных значений:", numbers)


#-----------------------------------------------------------------------------------------------------------------------


numbers = [5, 2, 3, 8, 4, 1, 2, 7]
new_numbers = []
even_numbers = []
count = 0

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
even_numbers.sort(reverse=True)

for i in numbers:
    if i % 2:
        new_numbers.append(i)
    else:
        new_numbers.append(even_numbers[count])
        count += 1

print("Список после сортировки:", new_numbers)








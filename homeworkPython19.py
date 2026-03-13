data = {"a": 1, "b": 2, "c": 1, "d": 3}
new_data = {}

for key, value in data.items():                                                           #1
    if value not in new_data:
        new_data[value] = [key]
    else:
        new_data[value] += [key]

print('Перевернутый словарь:', new_data)

#-----------------------------------------------------------------------------------------------------------------------

words = ["anna", "bennet", "john"]                                            #2.1
letter_counter = {}

for word in words:
    letter_counter[word] = {}
    for letter in word:
        letter_counter[word].update({letter: word.count(letter)})

print(letter_counter)

#-----------------------------------------------------------------------------------------------------------------------

words = ["anna", "bennet", "john"]
letter_counter = {}                                                             #2.2

for name in words:
    for letter in name:
        letter_counter.setdefault(name, {})[letter] = name.count(letter)

print(letter_counter)

#-----------------------------------------------------------------------------------------------------------------------

students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}             #3.1
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]
result = {}

for name, rate in students.items():

    if rate >= 85:
        result.setdefault(groups[0], {})[name] = rate
    elif rate >= 70:
        result.setdefault(groups[1], {})[name] = rate
    elif rate >= 50:
        result.setdefault(groups[2], {})[name] = rate
    else:
        result.setdefault(groups[3], {})[name] = rate

print(result)

#-----------------------------------------------------------------------------------------------------------------------

students = {"Аня": 92, "Боря": 76, "Ваня": 65, "Галя": 48, "Дима": 88, "Ева": 54}
groups = ["Отличники", "Хорошисты", "Троечники", "Не сдали"]                                  #3.2 итоговый вариант
result = {group: {} for group in groups}

for name, rate in students.items():

    if rate >= 85:
        result[groups[0]][name] = rate
    elif rate >= 70:
        result[groups[1]][name] = rate
    elif rate >= 50:
        result[groups[2]][name] = rate
    else:
        result[groups[3]][name] = rate

print(result)




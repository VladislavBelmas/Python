numbers = [4, 7, 3, 7, 8, 3, 4, 2, 7, 3, 8, 4]
all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
result = [i for i in all_nums if numbers.count(i) > 1]

print(f'Числа, встречающиеся более одного раза: {sorted(result, key=numbers.count ,reverse=True)}')

#-----------------------------------------------------------------------------------------------------------------------

dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2, "c": 3}

if set(dict1.values()) <= set(dict2.values()) or set(dict1.values()) >= set(dict2.values()):
    print("Один словарь является подмножеством второго.")
else:
    print("Один словарь не является подмножеством второго.")

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3", "Daisy")]      #2

def to_dict(diction):
    result = {}
    for key, value in diction:

        if key in result:
            result[key] += [value]
        else:
            result[key] = [value]

    return result


print(to_dict(students))

#-----------------------------------------------------------------------------------------------------------------------

from collections import defaultdict

def to_dict2(diction):
    result = defaultdict(list)
    for key, value in diction:

        result[key].append(value)


    return dict(result)


print(to_dict2(students))


#-----------------------------------------------------------------------------------------------------------------------
                                                                        #1
text = "Programming is fun!"
                                                                        #основной вариант
def char_counter(txt):
    return {c: (txt.lower().count(c))for c in txt.lower() if c.isalpha()}

print(char_counter(text))

#-----------------------------------------------------------------------------------------------------------------------

from collections import defaultdict

text = "Programming is fun!"

def char_counter2(txt):
    dd = defaultdict(int)
    for char in text.lower():
        if char.isalpha():
            dd[char] += 1
    return dict(dd)

print(char_counter2(text))

#-----------------------------------------------------------------------------------------------------------------------

from collections import Counter

text = "Programming is fun!"

def char_counter3(txt):
    return Counter(text.lower())

print(dict(char_counter3(text)))

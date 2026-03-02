set1 = {1, 2, 3, 4}                                                                             #1.1
set2 = {2, 3}
difference = set(set2 - set1)
if not difference:
    print("True")
else:
    print("False")

#-----------------------------------------------------------------------------------------------------------------------
                                                                                                #1.2
set1 = {1, 2, 3, 4}
set2 = {2, 3}

for item in set2:
    if item not in set1:
        print("False")
        break
else:
    print("True")

#-----------------------------------------------------------------------------------------------------------------------
                                                                                                #1.3
set1 = {1, 2, 3, 4}
set2 = {2, 3}

print(set1 >= set2)


#-----------------------------------------------------------------------------------------------------------------------
                                                                                                #2

set1 = {2, 3, 4, 5, 6}
set2 = {4, 5}

if set1 >= set2 or set1 <= set2:
    print("True")
    if len(set1) >= len(set2):
        print("Разница:", set1 - set2 if set(set1 - set2) else '-')
    else:
        print("Разница:", set2 - set1 if set(set2 - set1) else '-')
else:
    print("False")


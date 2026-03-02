grades = [5, 3, 4, 2, 1, 5, 3]                                              # 1
new_grades = []

for grade in grades:
    match grade:
        case _ if grade < 3:
            new_grades.append([grade, "неудовлетворительно"])
        case _ if grade < 5:
            new_grades.append([grade, "хорошо"])
        case _ :
            new_grades.append([grade, "отлично"])

print(new_grades)

#-----------------------------------------------------------------------------------------------------------------------
                                                                            # 1.1
new_grades2 = [ [grade, "неудовлетворительно"] if grade < 3 else
               ([grade, "хорошо"] if grade < 5 else [grade, "отлично"])
               for grade in grades ]

print(new_grades2)

#-----------------------------------------------------------------------------------------------------------------------

string = " ([ as(sa {}a(s)) d{}]b)      "     #({[}])   ([({}()){}])        # 2
brackets_from = [item for item in string if item in "{}[]()"]
stack = []
pairs = (("(", ")"), ("[", "]"), ("{", "}"))
variants_of_openers = "{[("

for item in brackets_from:
    if item in variants_of_openers:
        stack.append(item)
        continue

    if not stack:
        print("Несоответствие")
        break

    last_opener = stack.pop()

    if (last_opener, item) not in pairs:
        print("Несоответствие")
        break
else:
    print("Правильно" if not stack else "Несоответствие")






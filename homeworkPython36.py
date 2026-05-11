
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")


class Student(Person):
    def __init__(self, name, course_num):
        super().__init__(name)
        self.course_num = int(course_num)


    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course_num}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def introduce(self):
        print(f"Hello, I am professor {self.name}.\nMy subject is {self.subject}")


student = Student("Alice", "2")
teacher = Teacher("Bob", "Mathematics")

for person in (student, teacher):
    person.introduce()

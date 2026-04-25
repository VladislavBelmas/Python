import json
from datetime import datetime
from collections import defaultdict
students_per_course = defaultdict(int)
total_students = 0
ages = []
student_courses_report = dict()

with open("student_courses.json", "r") as f:
    data = json.load(f)

for record in data:
    total_students += 1

    birth = datetime.strptime(record["birth_date"], "%d.%m.%Y")
    enroll_date = datetime.strptime(record["enrollment_date"], "%d.%m.%Y")
    years = enroll_date.year - birth.year
    courses = record["courses"]

    ages.append(years if (enroll_date.month, enroll_date.day) > (birth.month, birth.day) else years - 1)

    for course in courses:
        students_per_course[course] += 1


mid_age = sum(ages) / total_students
students_per_course = dict(students_per_course)


student_courses_report.update({"total_students": total_students, "average_enrollment_age": mid_age,
                               "students_per_course":students_per_course})


with open("student_courses_report.json", "w", encoding="utf-8") as f:
    json.dump(student_courses_report, f, indent=4, sort_keys=True)


print("Completed")
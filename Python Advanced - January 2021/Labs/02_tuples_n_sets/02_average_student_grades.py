student_count = int(input())

students_grades_dict = {}
for _ in range(student_count):
    data = input().split()
    name, grade = data[0], float(data[1])
    if name not in students_grades_dict.keys():
        students_grades_dict[name] = [grade]
    else:
        students_grades_dict[name].append(grade)

students_grades = {}

for (name, grades) in students_grades_dict.items():
    grades_string = " ".join(map(lambda grade: f'{grade:.2f}', grades))
    average = sum(grades) / len(grades)
    print(f"{name} -> {grades_string} (avg: {average:.2f})")

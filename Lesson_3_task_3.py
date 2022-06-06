students = ["Alice", "Frank", "Michael", "Ivy", "Polina", "Bobby"]
grades = [85, 74, 90, 89, 100, 95, 78]

print(len(students))
print(len(grades))

if len(students) > len(grades):
    add = len(students) - len(grades)
    for i in range(add):
        grades.append(None)

if len(students) < len(grades):
    add = len(grades) - len(students)
    for i in range(add):
        grades.pop()


if len(students) == len(grades):
    res = {students[i]: grades[i] for i in range(len(students))}

    print(res)

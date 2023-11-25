students = []
course_to_search = None

while True:
    students_info = input()

    if ':' not in students_info:
        course_to_search = students_info
        break
    name, ID, course = students_info.split(':')
    students.append({'name': name, 'ID': ID, 'course': course})
for student in students:
    if course_to_search.startswith(student['course'][0:3]):
    # if course_to_search in students['course']:
        print(f'{student["name"]} - {student["ID"]}')
# print(students)
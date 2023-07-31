students = []
course_to_search = ''

while True:
    student_info = input()

    if ':' not in student_info:
        course_to_search = student_info
        break

    name, id, course = student_info.split(':')

    students.append({'name': name, 'id':id, 'course':course})

for student in students:
    if course_to_search.startswith(student['course'][0:3]):
        print(f"{student['name']} - {student['id']}")

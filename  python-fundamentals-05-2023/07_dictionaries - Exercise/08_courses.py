registered_students = {}

while True:
    entry = input()

    if entry == 'end':
        break

    course, name = entry.split(' : ')

    if course not in registered_students:
        registered_students[course] = []
    registered_students[course].append(name)

for key, value in registered_students.items():
    print(f'{key}: {len(registered_students[key])}')
    print('\n'.join(['-- ' + name for name in registered_students[key]]))

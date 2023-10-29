dictionary = {}
number = int(input())

for i in range(number):
    name = input()
    grade = float(input())

    if name not in dictionary:
        dictionary[name] = []
    dictionary[name].append(grade)

for key, value in dictionary.items():

    if len(value) >= 2:
        avg_grade = (value[0] + value[1]) / len(value)
        if avg_grade >= 4.50:
            print(f'{key} -> {avg_grade:.2f}')
    else:
        if value[0] >= 4.50:
            print(f'{key} -> {value[0]:.2f}')

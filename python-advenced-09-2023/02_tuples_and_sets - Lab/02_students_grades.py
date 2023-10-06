n = int(input())

students = {}

for _ in range(n):
    name, grade = input().split() # директно правим вход и разопаковане
    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for key, value in students.items(): # .items разопакова ключ и стойност
    formatted_value = ' '.join([f"{x:.2f}" for x in value])
    print(f"{key} -> {formatted_value} (avg: {(sum(value)/len(value)):.2f})")

# {' '.join(str(x) for x in value)} - вариант да се изпечатаме числа, вместо стрингове с компрехеншън, след като
# join изисква да са стрингове
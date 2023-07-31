employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
number_students = int(input())
time = 0

efficiency = employee_one + employee_two + employee_three
total_efficiency = 0

while number_students > 0:
    time += 1
    if time % 4 == 0:
        pass
    else:
        total_efficiency += efficiency
        number_students -= efficiency

print(f"Time needed: {time}h.")


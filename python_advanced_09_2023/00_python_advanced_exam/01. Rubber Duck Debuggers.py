from collections import deque

time_for_task = deque(int(x) for x in input().split(' '))
number_of_tasks = deque(int(x) for x in input().split(' '))

DARTH_VADER = 0
THOR = 0
BLUE_RUBBER = 0
YELLOW_RUBBER = 0

while time_for_task and number_of_tasks:
    task = number_of_tasks.pop()
    time = time_for_task.popleft()

    calculated_time = task * time

    if 0 < calculated_time < 61:
        DARTH_VADER += 1
    elif 60 < calculated_time < 121:
        THOR += 1
    elif 120 < calculated_time < 181:
        BLUE_RUBBER += 1
    elif 180 < calculated_time < 241:
        YELLOW_RUBBER += 1
    else:
        task -= 2
        number_of_tasks.append(task)
        time_for_task.append(time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

print(f"Darth Vader Ducky: {DARTH_VADER}")
print(f"Thor Ducky: {THOR}")
print(f"Big Blue Rubber Ducky: {BLUE_RUBBER}")
print(f"Small Yellow Rubber Ducky: {YELLOW_RUBBER}")

from project.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name):
        for task in self.tasks:
            if task == task_name:
                task.completed = True
                return f"Completed task {task_name}"
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count = 0
        for pos, tasks in enumerate(self.tasks):
            if tasks.completed:
                count += 1
                del self.tasks[pos]
        return f"Cleared {count} tasks."

    def view_section(self):
        text = f"Section {self.name}:\n"
        for show in self.tasks:
            text += f"{show.details()}\n"
        return text


daily_section = Section('Дневни дейности')
night_section = Section('Нощни дейности')

# описвам таскове
task = Task("Kъпане", "01/11/2023")
task3 = Task("Каране на кола", "03/11/2023")
task2 = Task("Спане", "02/11/2023")

# добавям add
daily_section.add_task(task)
print(daily_section.add_task(task))
daily_section.add_task(task3)
night_section.add_task(task2)
print(daily_section.complete_task(task))
print(night_section.complete_task(task2))

print(daily_section.clean_section())
print(night_section.clean_section())

print(daily_section.view_section())
print(night_section.view_section())

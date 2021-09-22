from project.task import Task


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        filtered_tasks = [t for t in self.tasks if t == new_task]
        if filtered_tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        filtered_tasks = [t for t in self.tasks if t.name == task_name]
        if not filtered_tasks:
            return f"Could not find task with the name {task_name}"
        task_name.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        completed_tasks = 0
        for t in self.tasks:
            if t.completed:
                self.tasks.remove(t)
                completed_tasks += 1
        return f"Cleared {completed_tasks} tasks."

    def view_section(self):
        section_details = f"Section {self.name}:\n"
        for t in self.tasks:
            section_details += t.details() + '\n'
        return section_details


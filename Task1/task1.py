import json
import os

class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Load tasks from the JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()

    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks available.")
        for idx, task in enumerate(self.tasks, start=1):
            status = "Done" if task["completed"] else "Pending"
            print(f"{idx}. {task['task']} - {status}")

    def update_task(self, task_id, new_task=None, mark_done=False):
        """Update a task (either change text or mark as completed)."""
        if 0 < task_id <= len(self.tasks):
            task = self.tasks[task_id - 1]
            if new_task:
                task["task"] = new_task
            if mark_done:
                task["completed"] = True
            self.save_tasks()
            print(f"Task {task_id} updated!")
        else:
            print(f"Task {task_id} not found.")

    def delete_task(self, task_id):
        """Delete a task from the list."""
        if 0 < task_id <= len(self.tasks):
            del self.tasks[task_id - 1]
            self.save_tasks()
            print(f"Task {task_id} deleted!")
        else:
            print(f"Task {task_id} not found.")

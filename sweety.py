import os
import json
from datetime import datetime

DATA_FILE = "todo_data.json"


class Task:
    def __init__(self, title, done=False, created_at=None):
        self.title = title
        self.done = done
        self.created_at = created_at or datetime.now().isoformat()

    def to_dict(self):
        return {
            "title": self.title,
            "done": self.done,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        return Task(
            title=data["title"],
            done=data.get("done", False),
            created_at=data.get("created_at")
        )


class ToDoApp:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(item) for item in data]

    def save_tasks(self):
        with open(DATA_FILE, "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=2)

    def add_task(self, title):
        self.tasks.append(Task(title))
        self.save_tasks()
        print(f"✅ Task added: {title}")

    def list_tasks(self):
        if not self.tasks:
            print("📭 No tasks found.")
            return
        print("\n📋 To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            status = "✅" if task.done else "❌"
            print(f"{i}. {status} {task.title} (Created: {task.created_at.split('T')[0]})")
        print()

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].done = True
            self.save_tasks()
            print(f"✔️ Marked task {index + 1} as done.")
        else:
            print("❗ Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks.pop(index)
            self.save_tasks()
            print(f"🗑️ Deleted task: {task.title}")
        else:
            print("❗ Invalid task number.")

    def clear_tasks(self):
        confirm = input("⚠️ Are you sure you want to delete all tasks? (y/n): ").lower()
        if confirm == 'y':
            self.tasks = []
            self.save_tasks()
            print("🧹 All tasks cleared.")
        else:
            print("Cancelled.")


def print_menu():
    print("\n====== To-Do Manager ======")
    print("1. List tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Clear all tasks")
    print("0. Exit")
    print("===========================\n")


def main():
    app = ToDoApp()
    while True:
        print_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            app.list_tasks()
        elif choice == "2":
            title = input("Enter task description: ").strip()
            if title:
                app.add_task(title)
            else:
                print("⚠️ Task cannot be empty.")
        elif choice == "3":
            app.list_tasks()
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                app.mark_done(index)
            except ValueError:
                print("⚠️ Invalid input.")
        elif choice == "4":
            app.list_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                app.delete_task(index)
            except ValueError:
                print("⚠️ Invalid input.")
        elif choice == "5":
            app.clear_tasks()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()

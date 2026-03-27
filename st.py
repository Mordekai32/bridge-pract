import json
from datetime import datetime

class Task:
    def __init__(self, title, priority, deadline):
        self.title = title
        self.priority = priority
        self.deadline = deadline
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "deadline": self.deadline,
            "completed": self.completed
        }


class TaskManager:
    def __init__(self, file="tasks.json"):
        self.file = file
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.file, "r") as f:
                data = json.load(f)
                tasks = []
                for t in data:
                    task = Task(t["title"], t["priority"], t["deadline"])
                    task.completed = t["completed"]
                    tasks.append(task)
                return tasks
        except:
            return []

    def save_tasks(self):
        with open(self.file, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def add_task(self, title, priority, deadline):
        try:
            datetime.strptime(deadline, "%Y-%m-%d")  # validate date
            task = Task(title, priority, deadline)
            self.tasks.append(task)
            self.save_tasks()
            print("✅ Task added!")
        except ValueError:
            print("❌ Invalid date format (Use YYYY-MM-DD)")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return

        # sort by priority
        sorted_tasks = sorted(self.tasks, key=lambda x: x.priority)

        for i, t in enumerate(sorted_tasks):
            status = "✔️" if t.completed else "❌"
            print(f"{i}. {t.title} | Priority: {t.priority} | Deadline: {t.deadline} | {status}")

    def complete_task(self, index):
        try:
            self.tasks[index].mark_complete()
            self.save_tasks()
            print("✅ Task marked as complete!")
        except IndexError:
            print("❌ Invalid task number")

    def search_task(self, keyword):
        found = [t for t in self.tasks if keyword.lower() in t.title.lower()]
        for t in found:
            print(f"🔍 {t.title} (Priority {t.priority})")


def main():
    manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Complete Task")
        print("4. Search Task")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            priority = int(input("Priority (1=High, 5=Low): "))
            deadline = input("Deadline (YYYY-MM-DD): ")
            manager.add_task(title, priority, deadline)

        elif choice == "2":
            manager.show_tasks()

        elif choice == "3":
            index = int(input("Task number: "))
            manager.complete_task(index)

        elif choice == "4":
            keyword = input("Search keyword: ")
            manager.search_task(keyword)

        elif choice == "5":
            print("Bye 👋")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
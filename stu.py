import json

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = int(age)  # typecasting
        self.grades = grades  # list

    def average(self):
        return sum(self.grades) / len(self.grades)

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "grades": self.grades
        }


class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_students()

    def load_students(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Student(**student) for student in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_students(self):
        with open(self.filename, "w") as file:
            json.dump([s.to_dict() for s in self.students], file, indent=4)

    def add_student(self, name, age, grades):
        try:
            grades = list(map(float, grades))
            student = Student(name, age, grades)
            self.students.append(student)
            self.save_students()
            print("✅ Student added successfully!")
        except ValueError:
            print("❌ Invalid input. Age or grades must be numbers.")

    def show_students(self):
        if not self.students:
            print("No students found.")
            return

        for s in self.students:
            print(f"Name: {s.name}, Age: {s.age}, Avg: {s.average():.2f}")


def main():
    manager = StudentManager()

    while True:
        print("\n--- Student Manager ---")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            name = input("Enter name: ")
            age = input("Enter age: ")
            grades = input("Enter grades (comma separated): ").split(",")

            manager.add_student(name, age, grades)

        elif choice == "2":
            manager.show_students()

        elif choice == "3":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
# student_tracker.py

students = {}

def add_student():
    name = input("Enter student name: ")
    grade = input("Enter grade: ")
    students[name] = grade
    print(f"{name}'s grade recorded.\n")

def view_students():
    if not students:
        print("No students found.\n")
        return
    for name, grade in students.items():
        print(f"{name}: {grade}")
    print()

def save_to_file():
    with open("students.txt", "w") as f:
        for name, grade in students.items():
            f.write(f"{name}:{grade}\n")
    print("Data saved to students.txt\n")

def load_from_file():
    try:
        with open("students.txt", "r") as f:
            for line in f:
                name, grade = line.strip().split(":")
                students[name] = grade
        print("Data loaded from students.txt\n")
    except FileNotFoundError:
        print("No saved file found. Starting fresh.\n")

def main():
    load_from_file()
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Save and Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            save_to_file()
            break
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    main()

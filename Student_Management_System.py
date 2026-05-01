class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")
        print("-" * 30)


students = []


def add_student():
    name = input("Enter name: ")
    roll = int(input("Enter roll no: "))
    marks = int(input("Enter marks: "))

    s = Student(name, roll, marks)
    students.append(s)

    print("Student Added Successfully\n")


def view_students():
    if not students:
        print("No students found\n")
        return

    for s in students:
        s.display()


def update_student():
    roll = int(input("Enter roll no to update: "))

    for s in students:
        if s.roll_no == roll:
            new_marks = int(input("Enter new marks: "))
            s.marks = new_marks
            print("Marks updated\n")
            return

    print("Student not found\n")


def delete_student():
    roll = int(input("Enter roll no to delete: "))

    for s in students:
        if s.roll_no == roll:
            students.remove(s)
            print("Student deleted\n")
            return

    print("Student not found\n")


while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice\n")
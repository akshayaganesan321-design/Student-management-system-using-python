import os

FILE_NAME = "students.txt"

def add_student():
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(name + "," + marks + "\n")

    print("Student record added successfully!\n")


def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found!\n")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

        if not data:
            print("File is empty!\n")
        else:
            print("\nStudent Records:")
            for line in data:
                name, marks = line.strip().split(",")
                print("Name:", name, "| Marks:", marks)
    print()


def search_student():
    name_to_search = input("Enter name to search: ")

    found = False
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, marks = line.strip().split(",")
                if name.lower() == name_to_search.lower():
                    print("Record Found →", name, marks)
                    found = True
                    break

    if not found:
        print("Student not found!\n")


def update_student():
    name_to_update = input("Enter name to update: ")

    if not os.path.exists(FILE_NAME):
        print("No file found!\n")
        return

    updated_lines = []
    found = False

    with open(FILE_NAME, "r") as file:
        for line in file:
            name, marks = line.strip().split(",")

            if name.lower() == name_to_update.lower():
                new_marks = input("Enter new marks: ")
                updated_lines.append(name + "," + new_marks + "\n")
                found = True
            else:
                updated_lines.append(line)

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_lines)

    if found:
        print("Record updated successfully!\n")
    else:
        print("Student not found!\n")


while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")

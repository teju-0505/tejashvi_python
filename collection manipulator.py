# Student Data Organizer

def display_welcome():
    print("Welcome to the Student Data Organizer!")
    print("You can add, view, update, and delete student records.\n")

students = []  # List to hold all student dictionaries
all_subjects = set()  # Set to hold all unique subjects

def add_student():
    name = input("Enter student's name: ")
    try:
        age = int(input("Enter student's age: "))
    except ValueError:
        print("Invalid age.")
        return
    grade = input("Enter student's grade: ")
    subjects = input("Enter subjects (comma-separated): ").split(',')
    subjects = {sub.strip() for sub in subjects}
    student_id = input("Enter student ID: ")
    dob = input("Enter date of birth (dd/mm/yyyy): ")

    all_subjects.update(subjects)

    student_data = {
        'id': student_id,
        'name': name,
        'age': age,
        'grade': grade,
        'subjects': subjects,
        'dob': dob
    }

    students.append(student_data)
    print("Student added successfully.")

def display_all_students():
    if not students:
        print("No student records available.")
        return
    print("\nAll Student Records:")
    for student in students:
        print(f"\nID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Grade: {student['grade']}")
        print(f"Subjects: {', '.join(student['subjects'])}")
        print(f"DOB: {student['dob']}")

def update_student():
    student_id = input("Enter the student ID to update: ")
    for student in students:
        if student['id'] == student_id:
            print("What do you want to update?")
            print("1. Age")
            print("2. Subjects")
            choice = input("Enter choice (1/2): ")
            if choice == '1':
                try:
                    new_age = int(input("Enter new age: "))
                    student['age'] = new_age
                    print("Age updated.")
                except ValueError:
                    print("Invalid input.")
            elif choice == '2':
                new_subjects = input("Enter new subjects (comma-separated): ").split(',')
                student['subjects'] = {sub.strip() for sub in new_subjects}
                all_subjects.update(student['subjects'])
                print("Subjects updated.")
            else:
                print("Invalid choice.")
            return
    print("Student ID not found.")

def delete_student():
    student_id = input("Enter student ID to delete: ")
    global students
    for student in students:
        if student['id'] == student_id:
            students.remove(student)
            print("Student deleted.")
            return
    print("Student not found.")

def display_subjects():
    if not all_subjects:
        print("No subjects found.")
    else:
        print("\nUnique Subjects Offered:")
        for subject in sorted(all_subjects):
            print(subject)

def main():
    display_welcome()
    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_subjects()
        elif choice == '6':
            print("Thank you for using the Student Data Organizer. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 to 6.")

if __name__ == "__main__":
    main()

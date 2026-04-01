# 

students = {}

while True:
    print("\n---- Student Grade ----")
    print("1. Add a new student")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in students:
            print(f"'{name}' already exists. Use option 2 to update their grade.")
        else:
            grade = input(f"Enter grade for {name}: ")
            students[name] = grade
            print(f"Student '{name}' added with grade '{grade}'.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            print(f"Current grade for '{name}': {students[name]}")
            new_grade = input(f"Enter new grade for {name}: ")
            students[name] = new_grade
            print(f"Grade updated to '{new_grade}' for '{name}'.")
        else:
            print(f"Student '{name}' not found. Use option 1 to add them.")

    elif choice == "3":
        if students:
            print("\n--- Student Grades ---")
            for name, grade in students.items():
                print(f"{name}: {grade}")
        else:
            print("No students found. Add some first!")

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
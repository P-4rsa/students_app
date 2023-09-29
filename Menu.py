# v 3.6.0

import student_operations as stdo


def menu():
   
    while True:
        
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        print("Welcome to the Student Management Program!")
        print("Please choose an option:")
        print("A: Add a student")
        print("F: Find a student")
        print("D: Delete a student")
        print("C: Change student courses")
        print("L: List all students")
        print("T: Show students table ")
        print("G: Show students grade distribution")
        print("S: Save data")
        print("Q: Quit the program")
        print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        choice = input("Enter your choice: ").upper()
        if choice == 'A':
            stdo.add_student()
        elif choice == 'F':
            stdo.find_student()
        elif choice == 'D':
            stdo.delete_student()
        elif choice == 'C':
            stdo.add_student_courses()
        elif choice == 'L':
            stdo.list_students()
        elif choice == 'S':
            stdo.save_students()
        elif choice == 'T':
            stdo.show_students_table()
        elif choice == 'G':
            stdo.show_grade_distribution()
        elif choice == 'Q':
            break
        else:
            print("Invalid choice. Please try again.")
           

if __name__ == '__main__':
    menu()


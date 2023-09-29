from datetime import datetime
from os import system
clear = lambda : system("cls")
from pickle import dump,load
from tabulate import tabulate
import matplotlib.pyplot as plt
import Shamsi2Miladi as shm
try:
    with open("active_students.info", "rb") as students_info:
        students = load(students_info)
except FileNotFoundError:
    students = []

try:
    with open("graduated_students.info", "rb") as graduated_students_info:
        graduated_students = load(graduated_students_info)
except FileNotFoundError:
    graduated_students = []

#function for covert string input to datetime formate(shamsi or miladi)


def get_birth_date():
    while True:
        calendar = input("Please enter the calendar you want to use (gregorian/jalali): ")
        if calendar.lower() == 'gregorian':
            try:
                birth_date_str = input("Please enter the student's birthdate in yyyy/mm/dd format, for example: 2023/05/09: ")
                birth_date = datetime.strptime(birth_date_str,'%Y/%m/%d')
                return birth_date
            except ValueError:
                print('The date entered is not in the correct format. Please enter the date in yyyy/mm/dd format.')
        elif calendar.lower() == 'jalali':
            try:
                birth_date_str = input("Please enter the student's birthdate in yyyy/mm/dd format, for example: 1402/02/19: ")
                jy, jm, jd = map(int, birth_date_str.split('/'))
                gy, gm, gd = shm.jalali_to_gregorian(jy, jm, jd)
                birth_date = datetime(gy, gm, gd)
                return birth_date
            except ValueError:
                print('The date entered is not in the correct format. Please enter the date in yyyy/mm/dd format.')

 #--------------------------Main------------------------------    


#this is for creating lists to add students 
students = []
grades = []
graduated_students = []

# this function allows user to add students information
def add_student():
    clear()
    global students
    student={}
  
    student["first_name"] = input("please enter the student's first name:")
    student["last_name"] = input("please enter the student's last name:")
        
    #this following function will get string from user and convert it to the date_time(%Y/%m/%d) format
    student["birth_date"] = get_birth_date()

    # Validate the code meli
    while True:
        code_meli = input("Please enter the student's code meli, the digit must be 10 numbers: ")
        if len(code_meli) != 10:
            print("Invalid code meli. The code meli must have 10 digits.")
        elif any(student["code_meli"] == code_meli for student in students):
            print("This code meli already exists. Please enter a unique code meli.")
        else:
            student["code_meli"] = code_meli
            break
    
    # Validate the student code
    while True:
        code = input("Please enter the student's code, the digit must be 5 numbers: ")
        if len(code) != 5:
            print("Invalid student code. The student code must have 5 digits.")
        elif any(student["code"] == code for student in students):
            print("This student code already exists. Please enter a unique student code.")
        else:
            student["code"] = code
            break
    

  # Ask the user to enter the course name and grade
    clear()       
    while True:
        course = input("Enter the student's course name: ")
        while True:
            try:
                grade = float(input("Enter the grade of the course: "))
                break
            except(ValueError):
                input("the grade should be a number,please try again")
            
        # Update the student dictionary with the course and grade
        student.update({course: grade})
        grades.append(grade)

            # Ask the user if they want to add more courses
        add_more = input("Do you want to add more courses? (yes/no) ")
        if add_more.lower() == 'no':
             break
    student["mean"] = sum(grades) / len(grades)
    
    students.append(student)
    input("Press any key")



def find_student():
    clear()
    code = input("Please enter the student's code: ")
    for student in students:
        if student["code"] == code:
            # Calculate the mean of grades
            # grades = [grade for course, grade in student.items() if course not in ["first_name", "last_name", "birth_date", "code_meli", "code"]]
            # mean = sum(grades) / len(grades)
            # Calculate the age of the student
            birth_date = (student["birth_date"])
            today = datetime.now()
            age = today.year - birth_date.year 
            # # Print the student's information
            print(f"First Name: {student['first_name']}")
            print(f"Last Name: {student['last_name']}")
            print(f"Birth Date: {student['birth_date']}")
            print(f"Code Melli: {student['code_meli']}")
            print(f"Code: {student['code']}")
            print(f"Mean of Grades: {student['mean']:.2f}")
            print(f"Age: {age}")
           
            return
    # If the code is not found, print an error message
    print("Student not found.")

def add_student_courses():
    clear()
    code = input("Please enter the student's code: ")
    for student in students:
        if student["code"] == code:
            while True:
                print("Courses and grades:")
                for key, value in student.items():
                    if key not in ["first_name", "last_name", "birth_date", "code_meli", "code", "mean"]:
                        print(f"{key}: {value}")
                action = input("Do you want to add or delete a course? (add/delete/exit): ")
                if action.lower() == "add":
                    course = input("Enter the course name: ")
                    while True:
                        try:
                            grade = float(input("Enter the grade: "))
                            student[course] = grade
                            break
                        except(ValueError):
                            input("The grade should be a number, please try again.")

                elif action.lower() == "delete":
                    course = input("Enter the course name: ")
                    if course in student:
                        del student[course]
                elif action.lower() == "exit":
                    break
graduated_students=[]
# this function allows user to delete or move students
def delete_student():
    clear()
    global graduated_students
    code = input("Enter the student code: ")
    for student in students:
        if student["code"] == code:
            option = input("Enter 'd' to delete the student or 'g' to move the student to graduated students: ")
            if option == 'd':
                students.remove(student)
                input("Student deleted successfully. Press any key")
                return
            elif option == 'g':
                graduated_students.append(student)
                students.remove(student)
                input("Student moved to graduated students successfully. Press any key")
                return
    input("Student not found. Press any key")


def list_students():
    clear()
    global students
    
    for student in students:
        print("Name: {} {}".format(student["first_name"], student["last_name"]))
        print("Birthdate: {}".format(student["birth_date"]))
        print("Code Meli: {}".format(student["code_meli"]))
        print("Code: {}".format(student["code"]))
        print("Courses and Grades:")
        for course, grade in student.items():
            if course not in ["first_name", "last_name", "birth_date", "code_meli", "code", "mean"]:
                print("- {}: {}".format(course, grade))
        print("Mean: {}".format(student["mean"]))
        print("----------------------------------------")
    input("Press any key")


def save_students():
    clear()
    try:
        with open("active_students.info", "wb") as students_info:
            dump(students, students_info)
        with open("graduated_students.info", "wb") as graduated_students_info:
            dump(graduated_students, graduated_students_info)
        input("Students and graduated students have been saved successfully.")
    except PermissionError:
        input("\n\nPlease choose another location to save the dataset.")


def show_students_table():
    # Ask the user which students to display
    while True:
        choice = input("Do you want to view active students, graduated students, or both? (active/graduated/both): ").lower()
        if choice in ['active', 'graduated', 'both']:
            break
        else:
            print("Invalid choice. Please try again.")
    # Convert the list of students into a list of dictionaries
    students_list = [student for student in students]
    # Add a 'Status' key to each student dictionary
    for student in students_list:
        student['Status'] = 'Active'
    # Convert the list of graduated students into a list of dictionaries
    graduated_students_list = [student for student in graduated_students]
    # Add a 'Status' key to each graduated student dictionary
    for student in graduated_students_list:
        student['Status'] = 'Graduated'
    # Create the list of students to display based on the user's choice
    if choice == 'active':
        all_students_list = students_list
    elif choice == 'graduated':
        all_students_list = graduated_students_list
    else:
        all_students_list = students_list + graduated_students_list
    # Create the table
    table = tabulate(all_students_list, headers='keys', tablefmt='fancy_grid')
    # Print the table
    print(table)
def show_grade_distribution():
    clear()
    # Ask the user which course to display
    course = input("Please enter the course name: ")
    # Get the grades for the specified course
    grades = [student[course] for student in students if course in student]
    # Create the bar chart
    plt.hist(grades)
    plt.title(f"Grade Distribution for {course}")
    plt.xlabel("Grade")
    plt.ylabel("Number of Students")
    # Display the bar chart
    plt.show()




                          

            



    
          



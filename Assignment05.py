# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   BPangan, 5/15/2024, Created Script
# ------------------------------------------------------------------------------------------ #

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course
    2. Show current data  
    3. Save data to a file
    4. Exit the program
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ''
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data

# When the program starts, read the file data into a list of lists (table)
#Need to import JSON file
import json
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    # Load JSON file into list
    students = json.load(file)
 #   print(students)
    file.close()
except FileNotFoundError as e:
    print("Enrollments file does not exist\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')\
    #creates JSON file if no file is found
    file = open(FILE_NAME, "w")
    print('Enrollment file created')
finally:
    file.close()

# Present and Process the data
while True:
    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")
    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            #error handling if first name is not alphanumeric
            if not student_first_name.isalpha():
                raise ValueError(' First name can only have alphabetic characters')
        except ValueError as e:
            print("User entered invalid first name. continuing.....")
        try:
            student_last_name = input("Enter the student's last name: ")
            # error handling if last name is not alphanumeric
            if not student_last_name.isalpha():
                raise ValueError(' Last name can only have alphabetic characters')
        except ValueError as e:
            print("User entered invalid Last name. continuing.....")
        finally:
            course_name = input("Please enter the name of the course: ")
            student_data: dict[str,str] = {'First Name': student_first_name, 'Last Name': student_last_name,
                                       'Course Name': course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        for student in students:
            print(f"{student['First Name']} {student['Last Name']} is enrolled in {student['Course Name']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students,file)
            file.close()
        #not sure if you would ever reach this exception unless file is deleted mid-run
        #maybe there is a more useful error handler?
        except FileNotFoundError as e:
            print("Enrollments file does not exist\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
            # creates JSON file if no file is found
            file = open(FILE_NAME, "w")
            print('Enrollment file created')
            json.dump(students, file)
        finally:
            file.close()
        print("The following data was saved to file!")
        for student in students:
            print(f"{student['First Name']} {student['Last Name']} is enrolled in {student['Course Name']}")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")

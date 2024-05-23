# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#  kamal,5/22/2024,Script Creation
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data
csv_data: str = ''  # Holds combined string data separated by a comma.
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.

# Creating classes
'''
    A collection of processing layer functions
    change log(who,when,what)
    kamal,05/22/24,first class creation
    '''

# Creating class FileProcessor
class FileProcessor:
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):

        try:
            file = open(file_name, "r")
            student_data = json.load(file)
            file.close()
        except Exception as e:
            print(e)
            print("File not found")
            print(e.__doc__)
            print(e.__str__())
        finally:
            if file.closed == False:
                file.close()
        return student_data

    @staticmethod
    # Creating function
    def write_data_to_file(file_name: str, student_data: list):
        try:
            file = open(file_name, "w")
            json.dump(student_data, file)
            file.close()
            print("Data written to file")
            for student in students:
                print(f'Student {student["FirstName"]} '
                      f'{student["LastName"]} is enrolled in {student["CourseName"]}')
                print("-" * 50)
        except Exception as e:
            if file.closed == False:
                file.close()
                IOProcessor.output_error_message(e)


# Creating second class
class IOProcessor:
    @staticmethod
    def output_error_message(message: str, exception: Exception = None): # Creating function output_error_message

        if exception is not None:
            print("-- Technical Error Message -- ")
            print(exception)  # Prints the custom message
            print(exception.__doc__)
            print(exception.__str__())

    @staticmethod
    def output_message(message: str):
        print(message)

    @staticmethod
    def output_menu(menu: str):
        print(menu, end='\n\n')

    @staticmethod
    def input_menu_choice():
        menu_choice = input("Enter your menu choice number: ")
        if menu_choice not in ['1', '2', '3', '4']:
            IOProcessor.output_message("Please enter an option between 1 and 4")
        return menu_choice

    @staticmethod
    def output_student_courses(student_data: list):
        print("-" * 50)
        for student in students:
            print(f'Student {student["FirstName"]} '
                  f'{student["LastName"]} is enrolled in {student["CourseName"]}')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print("-" * 50)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
            print("-" * 50)
        except ValueError as e:
            IOProcessor.output_error_message(e)
        except Exception as e:
            IOProcessor.output_error_message(e)
        return student_data


# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IOProcessor.output_menu(MENU)
    menu_choice = IOProcessor.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        IOProcessor.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":

        # Process the data to create and display a custom message
        print("-" * 50)
        IOProcessor.output_student_courses(student_data=students)
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":

        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)

        continue

    # Stop the loop
    elif menu_choice == "4":

        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")

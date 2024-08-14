# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   JBoardman, 8/12/2024, Updated script with Person & Student data classes and methods
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
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# (jb 8.12.24) created a Person Class
class Person:  # (jb 8.12.24) person data class
    """
    A collection of person data
    ChangeLog: (Who, When, What)
    JBoardman,8.12.2024, Created Class
    """

    # (jb 8.12.24) added first_name and last_name properties to the constructor
    # (jb 8.12.2024) intentionally not using 'student' here as this is a person and later could be a non-student
    def __init__(self, first_name: str = '', last_name: str = ''):  # (jb 8.12.24) created constructor
        """
        Initialize object and set first name and last name to blank string
        ChangeLog: (Who, When, What)
        JBoardman,8.12.2024, created method

        :param first_name: first name
        :param last_name: last name
        """
        self.first_name = first_name
        self.last_name = last_name

    # (jb 8.12.24) created a getter and setter for the first_name property
    @property
    def first_name(self):
        """
        Getter for first name with @property decorator
        ChangeLog: (Who, When, What)
        JBoardman,8.12.2024, created method
        :return: formatted name string
        """
        return self.__first_name.title()  # (jb 8.12.24) formatted name string, private

    @first_name.setter
    def first_name(self, value: str):
        """
        Setter for first name with validation
        ChangeLog: (Who, When, What)
        JBoardman,8.12.2024, created method
        :return: validated name string
        """
        if value.isalpha() or value == "":  # (jb 8.12.24) validate alpha or empty string
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    # (jb 8.12.24) created a getter and setter for the last_name property
    @property
    def last_name(self):
        """
        Getter for last name with @property decorator
        ChangeLog: (Who, When, What)
        JBoardman,8.12.2024, created method
        :return: formatted name string
        """
        return self.__last_name.title()

    @last_name.setter
    def last_name(self, value: str):
        """
        Setter for last name with validation
        ChangeLog: (Who, When, What)
        JBoardman,8.12.2024, created method
        :return: validated name string
        """
        if value.isalpha() or value == "":  # (jb 8.12.24) validate alpha or empty string, private
            self.__last_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    # (jb 8.12.24) Overrode the __str__() method to return Person data
    def __str__(self) -> str:
        """
        Presents object as a string, override default __str__ method
        ChangeLog: (Who, When, What)
        JBoardman,8.12.2024, override default method
        :return: object data as a string
        """
        return f"{self.first_name},{self.last_name}"


# (jb 8.12.24) Created a Student class the inherits from the Person class
class Student(Person):  # (jb 8.12.24) student data class
    """
    A collection of student data, where person data is inherited
    ChangeLog: (Who, When, What)
    JBoardman,8.12.2024, Created Class
    """

    # (jb 8.12.24) call to the Person constructor and pass it the first_name and last_name data
    def __init__(self, first_name: str = '', last_name: str = '', course_name: str = ''):  # (jb 8.12.24) + course_name
        """
        Initialize object & inherit from Person class
        ChangeLog: (Who, When, What)
        JBoardman,8.12.2024, created method

        :param first_name: first name
        :param last_name: last name
        :param course_name: course name
        """
        super().__init__(first_name=first_name, last_name=last_name)  # (jb 8.12.24) super() brings in the Person data

        # (jb 8.12.24) add an assignment to the course_name property using the course_name parameter (Done)
        self.course_name = course_name

# (jb 8.12.24) added the getter and setter for course_name
    @property
    def course_name(self):
        """
        Getter for course name with @property decorator
        ChangeLog: (Who, When, What)
        JBoardman,8.12.2024, created method
        :return: formatted name string
        """
        return self.__course_name  # (jb 8.12.24) private course name

    @course_name.setter
    def course_name(self, value: str):
        """
        Setter for course name
        ChangeLog: (Who, When, What)
        JBoardman,8.12.2024, created method
        :return: course name string
        """
        self.__course_name = value  # (jb 8.12.24) there is no validation here

# (jb 8.12.24) overrode the __str__() method to return the Student data
    def __str__ (self) -> str:  # (jb 8.12.24) object presented as a string
        """
        Presents object as a string, override default
        ChangeLog: (Who, When, What)
        JBoardman,8.12.2024, override default method
        :return: object data as a string
        """
        return f"{self.first_name},{self.last_name},{self.course_name}"


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files
    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    JBoardman,8.12.2024, added  processing dictionary and lists to use json with classes
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows
        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        JBoardman,8.12.2024, updated the read data from json file and save in a list for use with classes

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionary rows to be filled with file data

        :return: list
        """
        try:
            file = open(file_name, "r") # (jb 8.12.24) read from file
            # (jb 8.12.24) creating dictionary data from json
            list_of_dictionary_data = json.load(file)  # (jb 8.12.24) the load function returns a list of dictionary rows.
            for s_record in list_of_dictionary_data:  # (jb 8.12.24) Convert the list of dictionary rows into Student objects
                student_read = Student(first_name=s_record["FirstName"],
                                                last_name=s_record["LastName"],
                                                course_name=s_record["CourseName"])
                student_data.append(student_read)
            # (jb 8.12.24) close the file
            file.close()
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)
        finally:
            if file.closed == False:
                file.close()
        # (jb 8.12.24) return the list of students which will work with classes
        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows
        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        JBoardman, 8.12.2024, updated the write data to json file from dictionaries
        named the student_data to student_obj

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []  # (jb 8.12.24) define the list
            for s_record in student_data:  # (jb 8.12.24) convert List of Student objects to list of dictionary rows.
                # (jb 8.12.2024) student_json is a single row class and field (.dot notated) into the dictionary row
                student_json: dict \
                    = {"FirstName": s_record.first_name, "LastName": s_record.last_name, "CourseName": s_record.course_name}
                # (jb 8.12.2024) add the row to the dictionary
                list_of_dictionary_data.append(student_json)
            # (jb 8.12.2024) open the file in write moe
            file = open(file_name, "w")
            # (jb 8.12.2024) write the dictionary to the file
            json.dump(list_of_dictionary_data, file)
            file.close()
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output
    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
    RRoot,1.2.2030,Added menu output and input functions
    RRoot,1.3.2030,Added a function to display the data
    RRoot,1.4.2030,Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        RRoot,1.3.2030,Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        JBoardman, 8.12.2024, updated the print to use the student class .dot notation for fields

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:
            #  (jb 8.12.24) fixed this print statement to use the student object .dot notation
          print(f'   {student.first_name} {student.last_name} is registered for {student.course_name}.')
        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function
        JBoardman, 8.12.2024, updated to set create the student_new using the Student class

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")
            course_name = input("Please enter the name of the course: ")
            # (jb 8.12.24) changed to use the student object and fields
            # (jb 8.12.24) The first Student isn't required to run but is declaring the new_student will be a Student
            # (jb 8.12.24) works if I just have student_new = Student(first...
            student_new: Student = Student(first_name=student_first_name,
                                            last_name=student_last_name,
                                            course_name=course_name)
            # (jb 8.12.24) add the student object to the student data list
            student_data.append(student_new)
            print()
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        # (jb 8.12.24) updated this argument to pass in the students to the student_data list
        IO.output_student_and_course_names(student_data=students)
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

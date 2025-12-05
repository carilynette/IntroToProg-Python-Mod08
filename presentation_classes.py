# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08: Presentation Classes Module
# # Description: A collection of presentation classes for managing the application
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# CWilliams, 11/29/25, Moved classes into a module.
# ------------------------------------------------------------------------------------------------- #
from data_classes import Employee

class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    RRoot,1.1.2030,Created Class
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
        print()
        print(menu)
        print()


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
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_employee_data(employee_data: list):
        """ This function displays employee data to the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param employee_data: list of employee object data to be displayed

        :return: None
        """
        message:str = ''
        print()
        print("-" * 50)
        for employee in employee_data:
            if employee.review_rating == 5:
                message = "{} {} was rated on {} and is rated as {} (Leading)"
            elif employee.review_rating == 4:
                message = "{} {} was rated on {} and is rated as {} (Strong)"
            elif employee.review_rating == 3:
                message = "{} {} was rated on {} and is rated as {} (Solid)"
            elif employee.review_rating == 2:
                message = "{} {} was rated on {} and is rated as {} (Building)"
            elif employee.review_rating == 1:
                message = "{} {} was rated on {} and is rated as {} (Not Meeting Expectations)"

            print(message.format(employee.first_name,
                                 employee.last_name,
                                 employee.review_date.isoformat(),
                                 employee.review_rating))
        print("-" * 50)
        print()


    @staticmethod
    def input_employee_data(employee_data: list, employee_type: Employee):

        """ This function gets the first name, last name, review date and rating from the user

        ChangeLog: (Who, When, What)
        RRoot,1.1.2030,Created function

        :param employee_data: list of dictionary rows to be filled with input data

        :return: list
        """

        # Input the data
        employee_object = employee_type()

        while True:
            try:
                employee_object.first_name = input("What is the employee's first name? ")
                break
            except Exception as e:
                IO.output_error_messages("First Name Error. Use letters only.", e)

        while True:
            try:
                employee_object.last_name = input("What is the employee's last name? ")
                break
            except Exception as e:
                IO.output_error_messages("Last Name Error. Use letters only.", e)

        while True:
            try:
                employee_object.review_date = input("What is their review date (YYYY-MM-DD)?: ")
                break
            except Exception as e:
                IO.output_error_messages("Review Date Error. Date should be formatted YYYY-MM-DD.", e)

        while True:
            try:
                employee_object.review_rating = int(input("What is their review rating (1-5)? "))
                break
            except Exception as e:
                IO.output_error_messages("Review Rating Error. Review rating should be between 1 and 5", e)

        employee_data.append(employee_object)

        return employee_data

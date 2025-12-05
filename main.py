# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Working with Modules
# # Description: Demonstrates how to use code modules
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
#CWilliams, 11/29/25, Moved classes into modules.
# ------------------------------------------------------------------------------------------------- #

import data_classes as data
import processing_classes as proc
import presentation_classes as pres

# Beginning of the main body of this script
try:
    employees = proc.FileProcessor.read_employee_data_from_file(file_name=data.FILE_NAME,
                                                       employee_data=data.employees,
                                                       employee_type=data.Employee)  # Note this is the class name (ignore the warning)
except Exception as e:
    pres.IO.output_error_messages("Error loading data from file.",e)
    employees = data.employees


# Repeat the follow tasks
while True:
    pres.IO.output_menu(menu=data.MENU)

    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages("There was an error displaying current data",e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = pres.IO.input_employee_data(employee_data=employees, employee_type=data.Employee)  # Note this is the class name (ignore the warning)
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages("There was an error inputting new data.",e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=data.FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {data.FILE_NAME} file.")
        except Exception as e:
            pres.IO.output_error_messages("There was an error writing to file",e)
        continue

    elif menu_choice == "4":  # End the program
        break  # out of the while loop
